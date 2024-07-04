from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_divide_by_zero(calc_page):
    calc_page.fill_first_number(6)
    calc_page.fill_second_number(0)
    calc_page.click_divide()
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: Error"

def test_divide_by_negative_number(calc_page):
    calc_page.fill_first_number(10)
    calc_page.fill_second_number(-1)
    calc_page.click_divide()
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: -10"