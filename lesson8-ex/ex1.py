import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.wait_for_load_state(state=None, timeout=None)
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()

    # ---------------------
    input("Press anything to exit") # avoid stop running
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
