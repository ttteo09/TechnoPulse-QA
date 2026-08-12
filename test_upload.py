import pytest

# Simulăm backend-ul extins cu analiză de BPM
def process_audio_upload(file_name: str, file_bytes: bytes, bpm: int):
    audio_headers = [b'ID3', b'\xff\xfb', b'RIFF', b'fLaC']
    is_valid_audio = any(file_bytes.startswith(header) for header in audio_headers)

    if not is_valid_audio:
        return {
            "status_code": 400,
            "response": {"error": "Invalid audio format", "code": "ERR_INVALID_HEADER"}
        }

    # Logica de încadrare pe genul Techno
    is_techno_range = 120 <= bpm <= 165
    flag = "VALID_TECHNO" if is_techno_range else "OutOfTechnoRange"

    return {
        "status_code": 201,
        "response": {
            "message": "Track uploaded successfully",
            "bpm": bpm,
            "flag": flag
        }
    }


# --- TESTELE EXISTENTE ---

def test_upload_invalid_file_extension_renamed():
    fake_filename = "track_fals.mp3"
    fake_file_content = b"Acesta este doar un text simplu."
    result = process_audio_upload(fake_filename, fake_file_content, bpm=140)

    assert result["status_code"] == 400
    assert result["response"]["error"] == "Invalid audio format"

def test_upload_valid_mp3():
    valid_filename = "klangkuenstler_142bpm.mp3"
    valid_mp3_content = b"ID3v4...date_audio"
    result = process_audio_upload(valid_filename, valid_mp3_content, bpm=142)

    assert result["status_code"] == 201
    assert result["response"]["flag"] == "VALID_TECHNO"


# --- TEST NOU PARAMETRIZAT PENTRU BPM ---

@pytest.mark.parametrize("input_bpm, expected_flag", [
    (130, "VALID_TECHNO"),      # Peak Time Techno (Standard)
    (145, "VALID_TECHNO"),      # Hard Techno (Standard)
    (165, "VALID_TECHNO"),      # Limita superioară admisă
    (110, "OutOfTechnoRange"),  # Piesa prea lentă (House/Minimal)
    (180, "OutOfTechnoRange")   # Piesa prea rapidă (Gabber/Hardcore)
])
def test_bpm_range_validation(input_bpm, expected_flag):
    """
    TC-AUDIO-003: Verifică atribuirea tag-ului corect în funcție de valoarea BPM-ului.
    """
    valid_file_content = b"ID3v4...audio_data"
    result = process_audio_upload("track.mp3", valid_file_content, bpm=input_bpm)

    assert result["status_code"] == 201
    assert result["response"]["flag"] == expected_flag