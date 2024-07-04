import pytest
from playwright.sync_api import sync_playwright
from query_page import QueryPage

def test_success_query_performance():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        query_page = QueryPage(page)  # Initialize QueryPage with the Playwright page object
        query_page.navigate()  # Use navigate method from QueryPage
        query = "query { add(x: 10, y: 5) }"
        response = query_page.perform_query(query)  # Use perform_query method from QueryPage
        assert response['status'] == 200, f"Expected status code 200, got {response['status']}."
        assert response['data']['data']['add'] == 15, f"Expected add result to be 15, got {response['data']['data']['add']}."
        assert page.evaluate('performance.now()') < 300, "Response time is greater than 300 ms."

def test_failed_query_responsecode():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        query_page = QueryPage(page)  # Initialize QueryPage with the Playwright page object
        query_page.navigate()  # Use navigate method from QueryPage
        query = "query { add(x: 'aaa', y: 5) }"
        response = query_page.perform_query(query)  # Use perform_query method from QueryPage
        assert response['status'] == 400, f"Expected status code 400, got {response['status']}."