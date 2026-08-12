import pytest
import requests
from unittest.mock import patch, MagicMock

# URL-ul fictiv al serverului API TechnoPulse
API_URL = "https://api.technopulse.io/v1/tracks/upload"


# --- TEST API CU MOCKING ---

@patch("requests.post")
def test_api_upload_success(mock_post):
    """
    TC-API-001: Verifică răspunsul API-ului când încărcarea este reușită.
    """
    # 1. ARRANGE - Configurăm răspunsul fals (Mock) pe care îl va returna serverul
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        "id": "trk_99182",
        "title": "Industrial Sound",
        "bpm": 142,
        "status": "PROCESSED"
    }
    mock_post.return_value = mock_response

    # 2. ACT - Simulăm un request HTTP POST trimis de un client (Postman/Browser)
    payload = {"title": "Industrial Sound", "bpm": 142}
    response = requests.post(API_URL, json=payload)

    # 3. ASSERT - Verificăm dacă status code-ul și datele primite sunt corecte
    assert response.status_code == 201

    data = response.json()
    assert data["id"] == "trk_99182"
    assert data["bpm"] == 142
    assert data["status"] == "PROCESSED"


@patch("requests.post")
def test_api_upload_unauthorized(mock_post):
    """
    TC-API-002: Verifică respingerea cererii dacă utilizatorul nu este autentificat.
    """
    # ARRANGE
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.json.return_value = {"error": "Unauthorized", "message": "Missing API Key"}
    mock_post.return_value = mock_response

    # ACT
    response = requests.post(API_URL, json={})

    # ASSERT
    assert response.status_code == 401
    assert response.json()["error"] == "Unauthorized"