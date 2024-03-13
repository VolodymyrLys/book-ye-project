from selenium.webdriver.remote.webelement import WebElement
import time
from pages.base import BasePage
from pages.locators.registrationauthorization_locator import (
    RegistrationAuthorizationPageLocators,
)


class RegistrationAuthorizationPage(BasePage):
    def __init__(self, driver):
        """Initialize driver and objects to works with 'Registration-Authorization' page.

        :param driver: Remote
        """
        super().__init__(driver)

    def go_to_registration_page(self) -> WebElement:
        """Method which go to Rolls page.

        :return:WebElement
        """
        return self._driver.get("https://karuzo.ua/index.php?route=account/login")

    def authorization_form(self, login: str, password: str = None) -> None:
        """Method which fill authorization form

        :param: string
        :param: string
        :return:None
        """
        self._driver.find_element(
            *RegistrationAuthorizationPageLocators.LOCATOR_PHONE
        ).send_keys(login)
        time.sleep(5)
        self._driver.find_element(
            *RegistrationAuthorizationPageLocators.LOCATOR_PASSWORD
        ).send_keys(password)
        time.sleep(5)
        self._driver.find_element(
            *RegistrationAuthorizationPageLocators.LOCATOR_SUBMIT_BUTTON
        ).click()
        time.sleep(5)

    def log_out_from_account(self) -> None:
        """Method which log out from user account.

        :return: None
        """
        # self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_LOG_OUT).click()
