from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_simple_multiplication_with_integer(calc_page):
    calc_page.fill_first_number(6)
    calc_page.fill_second_number(5)
    calc_page.click_button("multiply")
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: 30"

def test_multiplication_by_negative_integer(calc_page):
    calc_page.fill_first_number(10)
    calc_page.fill_second_number(-1)
    calc_page.click_button("multiply")
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: -10"