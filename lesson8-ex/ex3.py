import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state(state=None, timeout=None)
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = page.get_by_role("checkbox")
    page.wait_for_timeout(3000)
    for i in range(checkboxes.count()):
        checkbox = checkboxes.nth(i)
        if (not checkbox.is_checked()):
            checkbox.check()

    # ---------------------+
    input("Press anything to exit")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
