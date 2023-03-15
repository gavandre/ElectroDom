import time

import pytest

from page_objects.home_page import HomePage
from test_data.registration_form_data import HomepageRegistration
from utilities import BaseClass


class Test_0001(BaseClass):
    """
        User is able to register new account using email address
        """

    def test_0001(self, get_data):
        log = self.getLogger()
        log.info("Opened https://electrodom.com.ua")
        home_page = HomePage(self.driver)
        home_page.click_on_vhid_button().click()
        log.info("Navigated to personal cabinet")
        home_page.click_on_registration_button()
        log.info("Started registration process")
        home_page.type_full_name(get_data["fullname"])
        log.info("Entered the full name" + get_data["fullname"])
        home_page.type_email(get_data["email"])
        log.info("Entered email address" + get_data["email"])
        home_page.type_pwd(get_data["password"])
        log.info("Entered password" + get_data["password"])
        home_page.clic_submit_btn()
        assert HomepageRegistration.popup_msg_text in home_page.get_success_message_text()
        log.info("Verified the popup message")
        time.sleep(10)

    @pytest.fixture(params=HomepageRegistration.full_name)
    def get_data(self, request):
        return request.param
