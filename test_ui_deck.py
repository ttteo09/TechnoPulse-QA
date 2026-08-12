import os
import pytest
from playwright.sync_api import Page, expect

# Calea către fișierul HTML local
HTML_PATH = f"file:///{os.path.abspath('index.html').replace('\\', '/')}"


def test_dj_deck_sync_button(page: Page):
    """
    TC-UI-001: Verifică dacă apăsarea butonului SYNC de pe Deck B
    potrivește BPM-ul cu cel din Deck A.
    """
    # 1. Deschidem pagina în browser
    page.goto(HTML_PATH)

    # 2. Verificăm că BPM-ul inițial pe Deck B este 128
    bpm_b = page.locator("#bpm-b")
    expect(bpm_b).to_have_text("128")

    # 3. Apăsăm butonul SYNC pe Deck B
    page.click("#sync-b")

    # 4. Verificăm că BPM-ul din Deck B s-a schimbat în 140 (sincronizat cu Deck A)
    expect(bpm_b).to_have_text("140")


def test_play_button_toggle_state(page: Page):
    """
    TC-UI-002: Verifică schimbarea stării vizuale la apăsarea butonului PLAY.
    """
    page.goto(HTML_PATH)

    play_btn = page.locator("#play-a")

    # Stare inițială: nu are clasa 'active'
    expect(play_btn).not_to_have_class("active")

    # Apăsăm butonul
    play_btn.click()

    # Verificăm că a primit clasa 'active'
    expect(play_btn).to_have_class("active")