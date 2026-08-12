import os
import pytest
from playwright.sync_api import Page, expect

# Formatare compatibilă cu orice sistem (Windows & Linux / CI-CD)
abs_path = os.path.abspath('index.html').replace('\\', '/')
HTML_PATH = f"file:///{abs_path}"


def test_dj_deck_sync_button(page: Page):
    """
    TC-UI-001: Verifică dacă apăsarea butonului SYNC de pe Deck B
    potrivește BPM-ul cu cel din Deck A.
    """
    page.goto(HTML_PATH)
    bpm_b = page.locator("#bpm-b")
    expect(bpm_b).to_have_text("128")
    page.click("#sync-b")
    expect(bpm_b).to_have_text("140")


def test_play_button_toggle_state(page: Page):
    """
    TC-UI-002: Verifică schimbarea stării vizuale la apăsarea butonului PLAY.
    """
    page.goto(HTML_PATH)
    play_btn = page.locator("#play-a")
    expect(play_btn).not_to_have_class("active")
    play_btn.click()
    expect(play_btn).to_have_class("active")