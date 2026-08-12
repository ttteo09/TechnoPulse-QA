import os
import librosa
import numpy as np
import pytest
import soundfile as sf


def generate_test_kick_track(
    filename="test_techno_140bpm.wav", bpm=140, duration_sec=4
):
    sr = 22050
    total_samples = sr * duration_sec
    audio = np.zeros(total_samples)

    beat_interval = 60.0 / bpm
    samples_per_beat = int(sr * beat_interval)

    for i in range(0, total_samples, samples_per_beat):
        kick_length = int(sr * 0.05)
        if i + kick_length < total_samples:
            t = np.linspace(0, 0.05, kick_length)
            audio[i : i + kick_length] = np.sin(2 * np.pi * 100 * t) * np.exp(
                -t * 30
            )

    sf.write(filename, audio, sr)
    return filename


def test_bpm_detection_accuracy():
    """TC-AUDIO-DSP-001: Verifică dacă algoritmul librosa detectează corect

    tempo-ul (BPM) dintr-un fișier audio generat.
    """
    target_bpm = 140
    audio_file = generate_test_kick_track(
        "techno_test.wav", bpm=target_bpm, duration_sec=6
    )

    try:
        y, sr = librosa.load(audio_file, sr=None)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

        # Conversie sigură din array NumPy
        detected_bpm = round(float(np.atleast_1d(tempo)[0]))

        # Toleranță de ±5 BPM ajustată pentru procesarea pe fișiere scurte
        assert (
            abs(detected_bpm - target_bpm) <= 5
        ), f"Expected {target_bpm} BPM, but got {detected_bpm}"

    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)