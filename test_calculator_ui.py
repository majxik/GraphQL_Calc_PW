from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_calculator_ui(calc_page):
    assert calc_page.is_add_button_present() == True
    assert calc_page.is_subtract_button_present() == True
    assert calc_page.is_multiply_button_present() == True
    assert calc_page.is_divide_button_present() == True
    assert calc_page.is_ac_button_present() == True
    assert calc_page.get_first_number() == '0'
    assert calc_page.get_second_number() == '0'
    assert calc_page.get_result() == 'Result: No result yet'
