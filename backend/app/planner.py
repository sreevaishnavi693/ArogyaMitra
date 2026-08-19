import os
from app.schemas import WellnessProfile, AdjustmentRequest


def workout_plan(profile: WellnessProfile) -> list[dict]:
    goal_focus = {
        "Weight Loss": "full-body cardio and strength",
        "Strength": "progressive resistance training",
        "Mobility": "mobility and core stability",
        "General Wellness": "balanced movement and recovery",
    }[profile.goal]
    sessions = ["Foundation", "Cardio", "Strength", "Mobility", "Intervals", "Recovery", "Reset"]
    exercises = {
        "Home": ["Bodyweight squats", "Incline push-ups", "Glute bridges", "Marching high knees"],
        "Gym": ["Leg press", "Cable row", "Chest press", "Treadmill walk"],
        "Outdoors": ["Brisk walk", "Step-ups", "Park bench push-ups", "Walking lunges"],
    }[profile.location]
    plan = []
    for index, title in enumerate(sessions):
        intensity = "Light" if title in {"Recovery", "Reset"} else ("Moderate" if profile.fitness_level == "Beginner" else "Challenging")
        selected = exercises[index % len(exercises):] + exercises[:index % len(exercises)]
        plan.append({
            "day": f"Day {index + 1}", "title": title, "duration": f"{profile.minutes_per_day} min",
            "intensity": intensity, "focus": goal_focus,
            "exercises": [f"Warm-up — 5 min", *[f"{item} — 3 sets" for item in selected[:3]], "Cool-down — 5 min"],
            "tip": "Keep the pace conversational and stop if you feel sharp pain." if title == "Recovery" else "Aim for steady, comfortable form over speed.",
        })
    return plan


def meal_plan(profile: WellnessProfile) -> list[dict]:
    avoid = ", ".join(profile.allergies) if profile.allergies else "none"
    meals = [
        ("Oats upma with fruit", "Dal, brown rice, and seasonal vegetables", "Moong chilla with mint chutney"),
        ("Poha with peas", "Rajma bowl with cucumber salad", "Vegetable khichdi"),
        ("Besan chilla", "Roti, chana masala, and salad", "Vegetable soup with millet toast"),
        ("Idli with sambar", "Tofu stir-fry with rice", "Palak dal with roti"),
        ("Overnight oats", "Vegetable pulao with raita alternative", "Chickpea salad wrap"),
        ("Fruit and seeds bowl", "Sambar rice with greens", "Tofu bhurji with roti"),
        ("Vegetable dosa", "Lentil curry with quinoa", "Light vegetable stew"),
    ]
    return [{"day": f"Day {i + 1}", "breakfast": x[0], "lunch": x[1], "dinner": x[2], "note": f"{profile.dietary_preference}; avoid: {avoid}."} for i, x in enumerate(meals)]


def adapt_plan(adjustment: AdjustmentRequest) -> dict:
    guidance = {
        "travel": "Swap equipment sessions for walking, hotel-room mobility, and short bodyweight circuits.",
        "injury": "Pause painful movements and choose gentle mobility; consult a qualified clinician for persistent pain.",
        "low_mood": "Reduce the barrier: take a ten-minute walk, stretch, and celebrate simply showing up.",
        "short_on_time": "Use a focused mini-session: warm up, three compound movements, and a short cool-down.",
    }[adjustment.situation]
    minutes = adjustment.minutes_available or 20
    return {"title": "AROMI adjusted your plan", "message": guidance, "new_duration": f"{minutes} min", "today": ["2 min breathing + warm-up", "3 rounds of 3 easy movements", "2 min stretch and hydration"], "detail": adjustment.details}


def coach_reply(message: str) -> str:
    lower = message.lower()
    if "travel" in lower:
        return "Travel mode activated: walk when possible, do a 15-minute mobility circuit, and carry a water bottle. Your consistency matters more than perfect sessions."
    if "pain" in lower or "injury" in lower:
        return "Let’s avoid anything that aggravates the area. I can suggest gentle alternatives, but sharp or persistent pain deserves advice from a qualified healthcare professional."
    return "I’m with you. Pick one small action for today: a glass of water, a 10-minute walk, or preparing your next balanced meal. Which feels most achievable?"

