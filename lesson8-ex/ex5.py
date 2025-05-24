import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/tables")
    page.wait_for_load_state(state=None, timeout=None)
    table1_rows = page.locator("#table1").get_by_role("row")
    result = ""
    for i in range (table1_rows.count()):
        row = table1_rows.nth(i)
        cells = row.locator("td, th")
        cells_text = cells.all_inner_texts()
        for word in cells_text:
            if ("edit" not in word or "delete" not in word):
                result += word + ","

        result += "\n"

    print(result)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
