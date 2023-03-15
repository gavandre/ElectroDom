import pytest

from page_objects.home_page import HomePage
from test_data.registration_form_data import HomepageRegistration
from utilities import BaseClass


class Test_0002(BaseClass):
    """
            User can't register new account using email address that was already registered
            """

    def test_0002(self, get_data, get_expired_data):
        log = self.getLogger()
        log.info("Opened https://electrodom.com.ua")
        home_page = HomePage(self.driver)
        home_page.click_on_vhid_button()
        log.info("Navigated to personal cabinet")
        home_page.click_on_registration_button()
        log.info("Started registration process")
        home_page.type_full_name(get_data["fullname"])
        log.info("Entered the full name" + get_data["fullname"])
        home_page.type_email(get_expired_data["email"])
        log.info("Entered expired email address")
        home_page.type_pwd(get_data["password"])
        log.info("Entered password" + get_data["password"])
        home_page.clic_submit_btn()
        assert home_page.get_error_message_text() in HomepageRegistration.expired_error_message


    @pytest.fixture(params=HomepageRegistration.full_name)
    def get_data(self, request):
        return request.param

    @pytest.fixture(params=HomepageRegistration.expired_email)
    def get_expired_data(self, request):
        return request.param
