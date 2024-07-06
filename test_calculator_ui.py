from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_calculator_ui(calc_page):
    assert calc_page.is_button_present("add") == True, "Add button should be present"
    assert calc_page.is_button_present("subtract") == True, "Subtract button should be present"
    assert calc_page.is_button_present("multiply") == True, "Multiply button should be present"
    assert calc_page.is_button_present("divide") == True, "Divide button should be present"
    assert calc_page.is_button_present("ac") == True, "AC button should be present"
    assert calc_page.get_first_number() == '0', "First number should be '0'"
    assert calc_page.get_second_number() == '0', "Second number should be '0'"
    assert calc_page.get_result() == 'Result: No result yet', "Result should be 'Result: No result yet'"
