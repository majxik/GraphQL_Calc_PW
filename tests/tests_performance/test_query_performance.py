import sys
sys.path.append('C:/development/Ataccama/calculator-test-automation/graphql_calc_pw')
import pytest
from playwright.sync_api import sync_playwright
from page_objects.query_page import QueryPage
#Author: Martin Maiksnar
#Basic Performance Testing for GraphQL API

def test_success_query_performance(query_page):
    query = "query { add(x: 10, y: 5) }"
    response = query_page.perform_query(query)
    assert response['status'] == 200, f"Expected status code 200, got {response['status']}."
    assert response['data']['data']['add'] == 15, f"Expected add result to be 15, got {response['data']['data']['add']}."
    assert query_page.page.evaluate('performance.now()') < 300, "Response time is greater than 300 ms."

def test_failed_query_responsecode(query_page):
    query = "query { add(x: 'aaa', y: 5) }"
    response = query_page.perform_query(query)
    assert response['status'] == 400, f"Expected status code 400, got {response['status']}."