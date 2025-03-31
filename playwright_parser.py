from playwright.sync_api import sync_playwright

def try_parse(url):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url)
            html = page.inner_html("html")

            print(f"Successfully fetched {url} using Playwright.")
            input("Press Enter to continue...")
            page.close()

            return html
        except Exception as e:
            print(f"Error fetching page: {e}")
            return None
            