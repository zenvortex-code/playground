from playwright.sync_api import sync_playwright


if __name__ == '__main__':
    # playground script snippet, used as alternative to debug tests
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # headless=False to see the browser
    context = browser.new_context()
    page = context.new_page()


