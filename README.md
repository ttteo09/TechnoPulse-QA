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
# 🎵 TechnoPulse QA Automation Suite

![QA Suite CI](https://github.com/ttteo09/TechnoPulse-QA/actions/workflows/tests.yml/badge.svg)

An **end-to-end Full-Stack QA Automation Framework** built with Python for **TechnoPulse**, a virtual audio engine and streaming platform.

The project combines **API testing, audio/DSP validation, UI automation, performance testing, and CI/CD** into a single automated QA suite.

## 🚀 Features

* 🧪 Automated API and backend testing
* 🎵 Audio processing and BPM/beat detection validation
* 🌐 End-to-end UI testing with Playwright
* ⚡ API mocking and HTTP status validation
* 📈 Performance and load testing with Locust
* 🔄 Automated CI/CD test execution with GitHub Actions
* 📊 HTML test reporting with `pytest-html`

## 🛠️ Tech Stack

| Area                    | Technology                      |
| ----------------------- | ------------------------------- |
| **Language**            | Python                          |
| **Test Runner**         | `pytest`                        |
| **Test Reporting**      | `pytest-html`                   |
| **Audio / DSP**         | `librosa`, `numpy`, `soundfile` |
| **API Testing**         | `requests`, `unittest.mock`     |
| **UI Automation**       | `Playwright`                    |
| **Performance Testing** | `Locust`                        |
| **CI/CD**               | GitHub Actions                  |
| **Environment**         | Ubuntu                          |

## 🏗️ Architecture

The framework is structured around multiple QA layers:

```text
                    ┌─────────────────────┐
                    │    TechnoPulse      │
                    │   Audio Platform    │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │ API Testing │      │ Audio / DSP │      │ UI Testing  │
   │  requests   │      │  librosa    │      │ Playwright  │
   └─────────────┘      └─────────────┘      └─────────────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                               ▼
                      ┌─────────────────┐
                      │  QA Validation  │
                      │     pytest      │
                      └────────┬────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
          ┌──────────────┐          ┌──────────────┐
          │   Locust     │          │ GitHub       │
          │ Performance  │          │ Actions CI   │
          └──────────────┘          └──────────────┘
```

## 📁 Project Structure

```text
TechnoPulse-QA/
│
├── .github/
│   └── workflows/
│       └── tests.yml              # GitHub Actions CI/CD pipeline
│
├── test_upload.py                 # Upload validation & BPM parameterization
├── test_api_upload.py             # API endpoints & HTTP status mocking
├── test_audio_engine.py            # Audio/DSP & beat detection tests
├── test_ui_deck.py                # Playwright E2E UI tests
│
├── locustfile.py                  # Performance & load testing
├── index.html                     # Virtual DJ Deck UI mockup
├── requirements.txt               # Python dependencies
└── README.md
```

## 🧪 Test Coverage

### 📤 Upload Validation

`test_upload.py`

* Validates upload request headers
* Tests BPM-related parameters
* Uses parameterized test scenarios
* Verifies expected behavior for different inputs

### 🔌 API Testing

`test_api_upload.py`

* Tests API endpoints
* Validates HTTP status codes
* Uses `unittest.mock` for isolated API testing
* Covers success and failure scenarios

### 🎧 Audio Engine Testing

`test_audio_engine.py`

* Validates audio processing functionality
* Uses `librosa` for audio analysis
* Tests BPM and beat detection
* Uses `numpy` and `soundfile` for audio data handling

### 🖥️ UI / E2E Testing

`test_ui_deck.py`

* End-to-end browser automation with Playwright
* Tests the Virtual DJ Deck interface
* Validates user interactions and UI behavior

### 📈 Performance Testing

`locustfile.py`

* Simulates concurrent users
* Tests application performance under load
* Helps identify API bottlenecks and scalability issues

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ttteo09/TechnoPulse-QA.git
cd TechnoPulse-QA
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## ▶️ Running the Tests

Run the complete test suite:

```bash
pytest
```

Generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

Run a specific test module:

```bash
pytest test_api_upload.py
```

```bash
pytest test_audio_engine.py
```

```bash
pytest test_ui_deck.py
```

## 📈 Running Performance Tests

Start Locust:

```bash
locust -f locustfile.py
```

Then open the Locust web interface and configure the desired number of users and spawn rate.

## 🔄 CI/CD

The project uses **GitHub Actions** to automatically execute the QA test suite on an Ubuntu runner.

The workflow is defined in:

```text
.github/workflows/tests.yml
```

The CI pipeline is designed to provide automated feedback whenever changes are pushed to the repository.

![QA Suite CI](https://github.com/ttteo09/TechnoPulse-QA/actions/workflows/tests.yml/badge.svg)

## 🎯 QA Strategy

The framework follows a layered testing approach:

```text
        ┌─────────────────────┐
        │    E2E / UI Tests   │
        ├─────────────────────┤
        │  API / Integration   │
        ├─────────────────────┤
        │  Audio / DSP Tests   │
        ├─────────────────────┤
        │   Unit Validation    │
        └─────────────────────┘
```

This approach helps validate the platform from both **individual components** and **real user workflows**, while also covering performance and continuous integration.

## 📌 Project Goals

The main goal of TechnoPulse QA is to demonstrate a modern, maintainable QA automation workflow covering:

* **Functional testing**
* **API testing**
* **Audio/DSP validation**
* **End-to-end testing**
* **Performance testing**
* **Test reporting**
* **Continuous Integration**

---

⭐ **TechnoPulse QA** — Automated testing for audio, APIs, UI, and performance.
