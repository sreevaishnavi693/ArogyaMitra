import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.schemas import WellnessProfile, AdjustmentRequest, CoachMessage
from app.planner import workout_plan, meal_plan, adapt_plan, coach_reply

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="ArogyaMitra API", version="1.0.0", lifespan=lifespan)
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/health")
def health():
    return {"status": "healthy", "service": "ArogyaMitra API"}


@app.post("/api/plans")
def generate_plans(profile: WellnessProfile):
    return {"profile": profile, "workouts": workout_plan(profile), "meals": meal_plan(profile), "source": "local-safe-planner" if not os.getenv("GROQ_API_KEY") else "groq-ready"}


@app.post("/api/plans/adjust")
def adjust(adjustment: AdjustmentRequest):
    return adapt_plan(adjustment)


@app.post("/api/coach")
def coach(payload: CoachMessage):
    return {"coach": "AROMI", "reply": coach_reply(payload.message)}

