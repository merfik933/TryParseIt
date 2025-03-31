from playwright.sync_api import sync_playwright

def try_parse(url):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url)
            content = page.content()

            print(f"Successfully fetched {url} using Playwright.")
            browser.close()

            return content
        except Exception as e:
            print(f"Error fetching page: {e}")
            return None
            