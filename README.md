# 🎵 TechnoPulse QA Automation Suite

![QA Suite CI](https://github.com/ttteo09/TechnoPulse-QA/actions/workflows/tests.yml/badge.svg)

End-to-end **QA Automation Framework** built in Python for **TechnoPulse**, a virtual audio engine & streaming platform.

## 🛠️ Tech Stack

* **Testing:** `pytest`, `pytest-html`
* **Audio/DSP:** `librosa`, `numpy`, `soundfile`
* **API:** `requests`, `unittest.mock`
* **UI:** `Playwright`
* **Performance:** `Locust`
* **CI/CD:** GitHub Actions

## 📁 Project Structure

```text
TechnoPulse-QA/
├── .github/workflows/tests.yml  # CI pipeline
├── test_upload.py               # Upload & BPM tests
├── test_api_upload.py           # API tests & mocking
├── test_audio_engine.py         # Audio/DSP tests
├── test_ui_deck.py              # Playwright E2E tests
├── locustfile.py                # Load testing
├── index.html                   # DJ Deck UI
└── requirements.txt             # Dependencies
```

## 🚀 Run Tests

```bash
pip install -r requirements.txt
playwright install
pytest
```

Generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## 🎯 Coverage

API • Audio/DSP • UI/E2E • Performance • CI/CD

