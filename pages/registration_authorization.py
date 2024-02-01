from selenium.webdriver.remote.webelement import WebElement

from pages.base import BasePage

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

    def authorization_form(self, login: str, password: str) -> None:
        """Method which fill authorization form

        :param: string
        :param: string
        :return:None
        """
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_USERNAME).send_keys(
            login)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_PASSWORD).send_keys(
            password)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_SUBMIT_BUTTON).click()

    def log_out_from_account(self) -> None:
        """Method which log out from user account.

        :return: None
        """
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_LOG_OUT).click()
