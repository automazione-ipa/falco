import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    page.get_by_role("button", name="Choose File").set_input_files("C:/Users/d.falco/Downloads/logs-insights-results.json")
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(3000)
    if page.get_by_role("heading", name="File Uploaded!") is not None:
        print("File uploaded successfully")

    # ---------------------
    input("Press anything to exit")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
