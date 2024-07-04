from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_subtract_negative_by_negative_integer(calc_page):
    calc_page.fill_first_number(-6)
    calc_page.fill_second_number(-5)
    calc_page.click_subtract()
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: -1"

def test_subtract_bellow_maximum_of_negative_integer(calc_page):
    calc_page.fill_first_number(-2147483648)
    calc_page.fill_second_number(1)
    calc_page.click_subtract()
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: -2147483649"