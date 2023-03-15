from selenium.webdriver.common.by import By


class BasketPage:

    def __init__(self, driver):
        self.driver = driver

    to_order_btn = (By.XPATH, "(//span[text()='Оформити замовлення'])[2]")

    def click_to_order_btn(self):
        return self.driver.find_element(*BasketPage.to_order_btn).click()