#Author: Martin Maiksnar
#This is the page object for the calculator page

class CalculatorPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("http://localhost:3001/")

    def fill_first_number(self, number):
        self.page.fill('input[type="text"]:nth-of-type(1)', str(number))

    def get_first_number(self):
        return self.page.input_value('input[type="text"]:nth-of-type(1)')

    def fill_second_number(self, number):
        self.page.fill('input[type="text"]:nth-of-type(2)', str(number))

    def get_second_number(self):
        return self.page.input_value('input[type="text"]:nth-of-type(2)')

    def click_add(self):
        self.page.click('text=Add')

    def is_add_button_present(self):
        return self.page.is_visible('text=Add')

    def click_subtract(self):
        self.page.click('text=Subtract')

    def is_subtract_button_present(self):
        return self.page.is_visible('text=Add')

    def click_multiply(self):
        self.page.click('text=Multiply')

    def is_multiply_button_present(self):
        return self.page.is_visible('text=Multiply')

    def click_divide(self):
        self.page.click('text=Divide')

    def is_divide_button_present(self):
        return self.page.is_visible('text=Divide')

    def click_ac(self):
        self.page.click('text=AC')   

    def is_ac_button_present(self):
        return self.page.is_visible('text=AC')

    def get_result(self):
        return self.page.text_content('h3')