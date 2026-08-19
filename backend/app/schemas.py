from typing import Literal
from pydantic import BaseModel, Field


class WellnessProfile(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    goal: Literal["Weight Loss", "Strength", "Mobility", "General Wellness"]
    location: Literal["Home", "Gym", "Outdoors"]
    minutes_per_day: int = Field(ge=10, le=120)
    fitness_level: Literal["Beginner", "Intermediate", "Advanced"] = "Beginner"
    dietary_preference: str = Field(default="Vegetarian", max_length=80)
    allergies: list[str] = Field(default_factory=list, max_length=10)
    health_notes: str = Field(default="", max_length=500)


class AdjustmentRequest(BaseModel):
    situation: Literal["travel", "injury", "low_mood", "short_on_time"]
    details: str = Field(default="", max_length=300)
    minutes_available: int | None = Field(default=None, ge=5, le=120)


class CoachMessage(BaseModel):
    message: str = Field(min_length=1, max_length=500)

