import inspect
import logging

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup_teardown")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


    def check_element_existence(self, element):
        try:
            locator_type, locator = element
            self.driver.find_element(locator_type, locator)
        except NoSuchElementException:
            return False
        return True
