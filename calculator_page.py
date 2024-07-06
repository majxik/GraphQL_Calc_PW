#Author: Martin Maiksnar
#This is the page object for the calculator page

class CalculatorPage:
    FIRST_NUMBER_INPUT = 'input[type="text"]:nth-of-type(1)'
    SECOND_NUMBER_INPUT = 'input[type="text"]:nth-of-type(2)'
    RESULT_SELECTOR = 'h3'
    BUTTON_TEXTS = {
        "add": "Add",
        "subtract": "Subtract",
        "multiply": "Multiply",
        "divide": "Divide",
        "ac": "AC"
    }

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("http://localhost:3001/")

    def fill_number(self, number, input_selector):
        self.page.fill(input_selector, str(number))

    def get_input_value(self, input_selector):
        return self.page.input_value(input_selector)

    def fill_first_number(self, number):
        self.fill_number(number, self.FIRST_NUMBER_INPUT)

    def get_first_number(self):
        return self.get_input_value(self.FIRST_NUMBER_INPUT)

    def fill_second_number(self, number):
        self.fill_number(number, self.SECOND_NUMBER_INPUT)

    def get_second_number(self):
        return self.get_input_value(self.SECOND_NUMBER_INPUT)

    def click_button(self, button_name):
        button_text = self.BUTTON_TEXTS.get(button_name.lower())
        if button_text:
            self.page.click(f'text={button_text}')

    def is_button_present(self, button_name):
        button_text = self.BUTTON_TEXTS.get(button_name.lower())
        if button_text:
            return self.page.is_visible(f'text={button_text}')
        return False

    def get_result(self):
        return self.page.text_content(self.RESULT_SELECTOR)