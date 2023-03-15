import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_objects.item_page import ItemPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    vhid_button = (By.CSS_SELECTOR, ".userbar__button-text")
    registration_button = (By.XPATH, "//span[text()='Реєстрація']")
    full_name = (By.NAME, "user[title]")
    email_field = (By.XPATH, "(//input[@name='user[email]'])[3]")
    pwd_field = (By.XPATH, "(//input[@type='password'])[2]")
    submit_button = (By.XPATH, "//input[@value='Зареєструватись']")
    popup_msg = (By.XPATH, "//div/p[@class='popup-msg']")
    expired_email_error_msg = (By.CSS_SELECTOR, ".form-error-box.errorBox-message")
    email_field_login_page = (By.XPATH, "(//input[@name='user[email]'])[2]")
    pwd_field_login_page = (By.XPATH, "(//input[@type='password'])[1]")
    submit_button_login_page = (By.XPATH, "//input[@value='Увійти']")
    context_menu_personal_data = (By.LINK_TEXT, "Особисті дані")
    search_field = (By.CSS_SELECTOR, ".search__input")
    dynamic_dropdown_list = (By.XPATH, "//li/a[@class='search-results__link']")




    def click_on_vhid_button(self):
        return self.driver.find_element(*HomePage.vhid_button).click()

    def click_on_registration_button(self):
        return self.driver.find_element(*HomePage.registration_button).click()

    def type_full_name(self, name):
        return self.driver.find_element(*HomePage.full_name).send_keys(name)

    def type_email(self, email):
        return self.driver.find_element(*HomePage.email_field).send_keys(email)

    def type_pwd(self, password):
        return self.driver.find_element(*HomePage.pwd_field).send_keys(password)

    def clic_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_button).click()

    def get_success_message_text(self):
        msg_text = self.driver.find_element(*HomePage.popup_msg).text
        return msg_text

    def get_error_message_text(self):
        msg_text = self.driver.find_element(*HomePage.expired_email_error_msg).text
        return msg_text

    def type_email_login(self, email):
        return self.driver.find_element(*HomePage.email_field_login_page).send_keys(email)

    def type_password_login(self, password):
        return self.driver.find_element(*HomePage.pwd_field_login_page).send_keys(password)

    def click_submit_btn_login(self):
        return self.driver.find_element(*HomePage.submit_button_login_page).click()

    def get_user_cabinet_options(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*HomePage.vhid_button)).perform()
        actions.click(self.driver.find_element(*HomePage.context_menu_personal_data)).perform()
        return self.driver

    def get_search_result(self, request, desired_item):
        try:
            self.driver.find_element(*HomePage.search_field).send_keys(request)
            search_items = self.driver.find_elements(*HomePage.dynamic_dropdown_list)
            for item in search_items:
                if desired_item in item.text:
                    item.click()
                else:
                    break
            return self.driver
        except StaleElementReferenceException:
            pass


