from selenium.webdriver.common.by import By


class OrderConfirmation:
    def __init__(self, driver):
        self.driver = driver


    phone_field = (By.XPATH, "//input[@name='Recipient[delivery_phone]']")

    def input_phone_number(self, phone_num):
        return self.driver.find_element(*OrderConfirmation.phone_field).send_keys(phone_num)