from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=spring-core+4.1.0.RELEASE")
    page.wait_for_load_state(state=None, timeout=None)
    table1_rows = page.locator("#TableWithRules").get_by_role("table").get_by_role("row")
    result = ""
    for i in range(table1_rows.count()):
        row = table1_rows.nth(i)
        cells = row.locator("td, th")
        cells_text = cells.all_inner_texts()
        for word in cells_text:
            if ("CVE" in word): # clickable link
                row.get_by_role("link").click()
                row.locator("#cve-view-json").click()

        result += "\n"

    print(result)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
