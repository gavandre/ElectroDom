from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class PersonalData:
    def __init__(self, driver):
        self.driver = driver

    first_and_lastname = (By.CSS_SELECTOR, "input[name='user[title]']")

    def check_element_existence(self, element):
        try:
            locator_type, locator = element
            self.driver.find_element(locator_type, locator)
        except NoSuchElementException:
            return False
        return True

