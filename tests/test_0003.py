import time

import pytest

from page_objects.home_page import HomePage
from page_objects.user_cabinet import PersonalData
from test_data.registration_form_data import HomepageRegistration
from utilities import BaseClass


class Test_0003(BaseClass):
    """
    User can authenticate to his account
        """
    def test_0003(self, get_data):
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
        time.sleep(4)
        home_page.get_user_cabinet_options()
        log.info("User navigated to the personal data page")
        user_cabinet = PersonalData(self.driver)
        assert user_cabinet.check_element_existence(PersonalData.first_and_lastname)
        log.info("The firstname and Lastname field are present on the page in order to check whether user indeed has logged in")

    @pytest.fixture(params=HomepageRegistration.full_name)
    def get_data(self, request):
        return request.param
