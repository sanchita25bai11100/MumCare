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
from app.mood_engine import assess_mood


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
    Process a mood check-in and return supportive guidance.
    """

    assessment = assess_mood(request.mood)

    return {
        "reported_mood": request.mood,
        "support_level": assessment.level.value,
        "response": assessment.response,
        "medical_disclaimer": (
            "This feature provides general emotional support "
            "and does not diagnose mental-health conditions."
        ),
    }
