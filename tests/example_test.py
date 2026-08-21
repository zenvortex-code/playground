import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_search_docs(page: Page):
    page.goto("https://playwright.dev/")

    # Click the search button
    page.get_by_label("Search").click()

    # Type in search box
    page.get_by_placeholder("Search docs").fill("locators")

    # Verify search results appear
    expect(page.get_by_role("link", name=re.compile("Locators", re.IGNORECASE)).first).to_be_visible()

def test_navigation_menu(page: Page):
    page.goto("https://playwright.dev/")

    # Verify main navigation links are present
    expect(page.get_by_role("link", name="Docs", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="MCP", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="CLI", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="API", exact=True)).to_be_visible()
