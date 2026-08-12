# 🎵 TechnoPulse QA Automation Suite

![QA Suite CI](https://github.com/ttteo09/TechnoPulse-QA/actions/workflows/tests.yml/badge.svg)

An end-to-end Full-Stack QA Automation Framework built in Python for **TechnoPulse**, a virtual audio engine & streaming platform.

## 🛠️ Tech Stack & Architecture

- **Test Runner:** `pytest`, `pytest-html`
- **Audio DSP Engine:** `librosa`, `numpy`, `soundfile`
- **API Testing:** `requests`, `unittest.mock`
- **UI Automation:** `playwright`
- **Performance Testing:** `locust`
- **CI/CD Pipeline:** GitHub Actions (Ubuntu runner)

## 📁 Project Structure

TechnoPulse-QA/
├── .github/workflows/
│   └── tests.yml            # CI/CD Pipeline configuration
├── test_upload.py           # Header validation & BPM parameterization
├── test_api_upload.py       # API endpoints & HTTP status mocking
├── test_audio_engine.py     # Librosa & DSP beat detection
├── test_ui_deck.py          # Playwright E2E UI tests
├── locustfile.py            # Performance & load testing script
├── index.html               # Virtual DJ Deck UI mockup
└── requirements.txt         # Project dependencies
