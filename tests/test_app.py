from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "MumCare"
    assert response.json()["status"] == "operational"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_high_risk_symptom():
    response = client.post(
        "/api/v1/symptoms/assess",
        json={"symptom": "difficulty breathing"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["risk_level"] == "high"
    assert data["recommended_action"] == (
        "seek_urgent_professional_attention"
    )


def test_moderate_risk_symptom():
    response = client.post(
        "/api/v1/symptoms/assess",
        json={"symptom": "persistent headache"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["risk_level"] == "moderate"


def test_low_risk_symptom():
    response = client.post(
        "/api/v1/symptoms/assess",
        json={"symptom": "mild tiredness"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["risk_level"] == "low"


def test_mood_check_in():
    response = client.post(
        "/api/v1/mood/check-in",
        json={"mood": "I feel anxious"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["support_level"] == "supportive_check_in"
    assert "response" in data
