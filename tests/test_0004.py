import time

import pytest

from page_objects.basket_page import BasketPage
from page_objects.home_page import HomePage
from page_objects.item_page import ItemPage
from page_objects.order_comfirmation_page import OrderConfirmation
from test_data.registration_form_data import HomepageRegistration
from utilities import BaseClass


class OrderComfirmation:
    pass


class Test_004(BaseClass):

    def test_0004(self, get_data):
        log = self.getLogger()
        log.info("Opened https://electrodom.com.ua")
        home_page = HomePage(self.driver)
        home_page.click_on_vhid_button()
        log.info("User has entered into personal cabinet")
        home_page.type_email_login(get_data["email"])
        log.info("Email successfully entered")
        home_page.type_password_login(get_data["password"])
        log.info("Password successfully entered")
        home_page.click_submit_btn_login()
        log.info("Users mil and password submitted")
        time.sleep(3)
        home_page.get_search_result("grill", HomepageRegistration.desired_item)
        log.info("User has chosen the desired item")
        item_page = ItemPage(self.driver)
        self.check_element_existence(item_page.buy_button)
        item_page.click_buy_btn()
        log.info("User clicked on the 'Купити' button")
        basket_page = BasketPage(self.driver)
        basket_page.click_to_order_btn()
        order_page = OrderConfirmation(self.driver)
        order_page.input_phone_number(get_data["phone"])


        time.sleep(10)
    @pytest.fixture(params=HomepageRegistration.full_name)
    def get_data(self, request):
        return request.param
