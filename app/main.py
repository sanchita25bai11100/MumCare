"""
MumCare
AI-Assisted Maternal Care Support API

Academic prototype demonstrating:
- Symptom risk guidance
- Mood support
- Health document information extraction

This system provides guidance only and does not diagnose,
prescribe medication, or replace healthcare professionals.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from app.risk_engine import assess_symptom


app = FastAPI(
    title="MumCare API",
    description=(
        "AI-assisted maternal care support platform for "
        "risk-aware guidance, emotional support, and health information."
    ),
    version="1.0.0",
)


class SymptomRequest(BaseModel):
    symptom: str


class MoodRequest(BaseModel):
    mood: str


@app.get("/")
def root():
    """Health check for the MumCare API."""
    return {
        "name": "MumCare",
        "status": "operational",
        "message": "Maternal care support API is running.",
    }


@app.get("/health")
def health_check():
    """Return API health status."""
    return {
        "status": "healthy",
        "service": "mumcare-api",
    }


@app.post("/api/v1/symptoms/assess")
def symptom_assessment(request: SymptomRequest):
    """
    Analyze a reported symptom and return an advisory
    risk category with an appropriate next action.
    """

    assessment = assess_symptom(request.symptom)

    return {
        "symptom": request.symptom,
        "risk_level": assessment.level.value,
        "recommended_action": assessment.action,
        "guidance": assessment.message,
        "medical_disclaimer": (
            "This is an AI-assisted prototype and is not "
            "a medical diagnosis."
        ),
    }


@app.post("/api/v1/mood/check-in")
def mood_check_in(request: MoodRequest):
    """
    Provide a simple supportive response based on a
    user's emotional check-in.
    """

    mood = request.mood.lower().strip()

    if any(word in mood for word in ["sad", "lonely", "alone", "upset"]):
        response = (
            "It sounds like you may be going through a difficult moment. "
            "You do not have to handle everything alone. Consider reaching "
            "out to someone you trust or a qualified mental-health professional."
        )

        support_level = "additional_support_recommended"

    elif any(word in mood for word in ["anxious", "anxiety", "worried", "stress"]):
        response = (
            "It is understandable to feel worried or stressed. "
            "Consider taking a short pause, practicing slow breathing, "
            "and speaking with someone you trust if these feelings continue."
        )

        support_level = "supportive_check_in"

    elif any(word in mood for word in ["happy", "good", "great", "calm"]):
        response = (
            "That is wonderful to hear. Keep checking in with yourself "
            "and continue activities that support your well-being."
        )

        support_level = "positive"

    else:
        response = (
            "Thank you for checking in. Your emotional well-being matters. "
            "You can continue monitoring how you feel and seek support "
            "whenever you need it."
        )

        support_level = "general_support"

    return {
        "reported_mood": request.mood,
        "support_level": support_level,
        "response": response,
        "medical_disclaimer": (
            "This feature provides general emotional support and "
            "does not diagnose mental-health conditions."
        ),
    }
