from selenium.webdriver.common.by import By
from selenium.common import exceptions



class ItemPage:

    def __init__(self, driver):
        self.driver = driver

    buy_button = (By.XPATH, "(//span[@class='btn-content'])[3]")

    def click_buy_btn(self):
        self.driver.find_element(*ItemPage.buy_button).click()
        return self.driver
