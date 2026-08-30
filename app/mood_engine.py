"""
MumCare Mood Intelligence Engine

Provides lightweight emotional-support responses based on
user-reported mood signals.

This component does not diagnose mental-health conditions.
It is intended only for supportive check-ins.
"""

from dataclasses import dataclass
from enum import Enum


class SupportLevel(str, Enum):
    POSITIVE = "positive"
    SUPPORTIVE = "supportive_check_in"
    ADDITIONAL_SUPPORT = "additional_support_recommended"


@dataclass
class MoodAssessment:
    level: SupportLevel
    response: str


MOOD_SIGNALS = {
    SupportLevel.ADDITIONAL_SUPPORT: {
        "sad",
        "lonely",
        "alone",
        "hopeless",
        "upset",
    },
    SupportLevel.SUPPORTIVE: {
        "anxious",
        "anxiety",
        "worried",
        "stress",
        "stressed",
        "overwhelmed",
    },
    SupportLevel.POSITIVE: {
        "happy",
        "good",
        "great",
        "calm",
        "excited",
        "relaxed",
    },
}


def assess_mood(mood: str) -> MoodAssessment:
    """Convert a mood check-in into a supportive response."""

    if not mood or not mood.strip():
        return MoodAssessment(
            level=SupportLevel.SUPPORTIVE,
            response=(
                "Thank you for checking in. "
                "You can share how you are feeling whenever you are ready."
            ),
        )

    normalized = mood.lower().strip()

    if any(signal in normalized for signal in MOOD_SIGNALS[
        SupportLevel.ADDITIONAL_SUPPORT
    ]):
        return MoodAssessment(
            level=SupportLevel.ADDITIONAL_SUPPORT,
            response=(
                "It sounds like you may be having a difficult moment. "
                "You do not have to handle everything alone. Consider "
                "talking to someone you trust or a qualified professional."
            ),
        )

    if any(signal in normalized for signal in MOOD_SIGNALS[
        SupportLevel.SUPPORTIVE
    ]):
        return MoodAssessment(
            level=SupportLevel.SUPPORTIVE,
            response=(
                "It is understandable to feel worried or overwhelmed. "
                "Consider taking a short pause, practicing slow breathing, "
                "and reaching out to someone you trust if these feelings continue."
            ),
        )

    if any(signal in normalized for signal in MOOD_SIGNALS[
        SupportLevel.POSITIVE
    ]):
        return MoodAssessment(
            level=SupportLevel.POSITIVE,
            response=(
                "That is wonderful to hear. Keep checking in with yourself "
                "and continue activities that support your well-being."
            ),
        )

    return MoodAssessment(
        level=SupportLevel.SUPPORTIVE,
        response=(
            "Thank you for checking in. Your emotional well-being matters. "
            "Keep monitoring how you feel and reach out for support whenever "
            "you feel you need it."
        ),
    )
