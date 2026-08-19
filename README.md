# ArogyaMitra

An AI-assisted wellness planner that turns a person's goals, dietary preferences, time availability, and changing circumstances into practical workout and nutrition guidance.

## Stack

- **Frontend:** React + Vite
- **Backend:** FastAPI + SQLite
- **AI:** Groq-compatible chat-completions integration (with safe local fallback plans)
- **Security:** JWT-ready authentication endpoints, CORS configuration, and Pydantic validation

## Run locally

### Backend

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload --port 8000
```

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

Set `VITE_API_URL` in `frontend/.env` if the API is hosted elsewhere. To use Groq, add `GROQ_API_KEY` to `backend/.env`; without it the application uses a transparent local demonstration plan.

## Core workflows

1. Create a profile with fitness goal, preferred location, available minutes, and dietary needs.
2. Generate a 7-day workout plan and a nutrition plan.
3. Send a change (travel, injury, mood, or less time) to AROMI to adapt the routine.

