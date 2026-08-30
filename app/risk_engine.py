"""
MumCare Risk Intelligence Engine

A transparent, rule-based decision-support layer that
categorizes reported symptoms into guidance levels.

IMPORTANT:
This prototype does not diagnose medical conditions
or prescribe treatment.
"""

from dataclasses import dataclass
from enum import Enum


class RiskLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"


@dataclass
class RiskAssessment:
    level: RiskLevel
    action: str
    message: str


# Symptoms/signals that should trigger urgent professional attention.
HIGH_RISK_SIGNALS = {
    "heavy bleeding",
    "severe bleeding",
    "difficulty breathing",
    "severe chest pain",
    "loss of consciousness",
    "seizure",
    "severe abdominal pain",
}


# Signals that should generally be discussed with a healthcare professional.
MODERATE_RISK_SIGNALS = {
    "persistent vomiting",
    "persistent headache",
    "fever",
    "dizziness",
    "blurred vision",
    "swelling",
    "persistent pain",
}


def assess_symptom(symptom: str) -> RiskAssessment:
    """
    Assess a user-reported symptom using transparent
    prototype rules.

    Returns:
        RiskAssessment containing risk level, action,
        and user-facing guidance.
    """

    if not symptom or not symptom.strip():
        return RiskAssessment(
            level=RiskLevel.MODERATE,
            action="provide_more_information",
            message=(
                "Please provide more information about the symptom "
                "so appropriate guidance can be provided."
            ),
        )

    normalized = symptom.lower().strip()

    # Highest-priority safety check.
    for signal in HIGH_RISK_SIGNALS:
        if signal in normalized:
            return RiskAssessment(
                level=RiskLevel.HIGH,
                action="seek_urgent_professional_attention",
                message=(
                    "This symptom may require urgent medical attention. "
                    "Please contact a qualified healthcare professional "
                    "or your local emergency service."
                ),
            )

    # Secondary consultation check.
    for signal in MODERATE_RISK_SIGNALS:
        if signal in normalized:
            return RiskAssessment(
                level=RiskLevel.MODERATE,
                action="contact_healthcare_professional",
                message=(
                    "Consider discussing this symptom with a qualified "
                    "healthcare professional, especially if it persists "
                    "or becomes worse."
                ),
            )

    # No predefined risk signal detected.
    return RiskAssessment(
        level=RiskLevel.LOW,
        action="monitor_and_seek_advice_if_needed",
        message=(
            "No high-risk signal was detected by this prototype. "
            "Continue monitoring how you feel and seek professional "
            "advice if the symptom persists, worsens, or concerns you."
        ),
    )
