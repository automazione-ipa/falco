import re
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
import os


def run(playwright: Playwright) -> None:
    load_dotenv()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dipendenti.alfasoft.it/login")
    page.get_by_role("textbox", name="email").click()
    page.get_by_role("textbox", name="email").fill(os.getenv("MAIL"))
    page.get_by_role("textbox", name="email").press("Tab")
    page.get_by_role("textbox", name="password").fill(os.getenv("PASS"))
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(1000)
    page.locator(".mat-radio-outer-circle").first.click()

    # ---------------------
    input()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
