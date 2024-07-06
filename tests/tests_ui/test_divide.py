import sys
sys.path.append('C:/development/Ataccama/calculator-test-automation/graphql_calc_pw')
from playwright.sync_api import sync_playwright
from page_objects.calculator_page import CalculatorPage

#Author: Martin Maiksnar
#test for the divide operation

def test_divide_by_zero(calc_page):
    calc_page.fill_first_number(6)
    calc_page.fill_second_number(0)
    calc_page.click_button("divide")
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: Error"

def test_divide_by_negative_number(calc_page):
    calc_page.fill_first_number(10)
    calc_page.fill_second_number(-1)
    calc_page.click_button("divide")
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: -10"