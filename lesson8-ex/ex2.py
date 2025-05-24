import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state(state=None, timeout=None)
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(3):
        page.get_by_role("button", name="Add Element").click()
    
    buttons = page.get_by_role("button", name="Delete")
    if (buttons.count() == 3):
        print("3 buttons created")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
