import sys
sys.path.append('C:/development/Ataccama/calculator-test-automation/graphql_calc_pw')
from playwright.sync_api import sync_playwright
from page_objects.calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_invalid_input_with_text(calc_page):
    calc_page.fill_first_number('aaa')
    calc_page.fill_second_number(1)
    calc_page.click_button("add")
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: Error"

def test_invalid_input_with_blank(calc_page):
    calc_page.fill_first_number(1)
    calc_page.fill_second_number('')
    calc_page.click_button("add")
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: Error"