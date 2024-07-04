from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_simple_addition_with_integer(calc_page):
    calc_page.fill_first_number(9)
    calc_page.fill_second_number(11)
    calc_page.click_add()
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: 20"

def test_simple_addition_with_float(calc_page):
    calc_page.fill_first_number(9.5)
    calc_page.fill_second_number(10.5)
    calc_page.click_add()
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: 20"