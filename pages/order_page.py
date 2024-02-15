


class PizzaPage(BasePage):
    def pizza_form(self, login: str, password: str = None) -> None:
        """Method which fill authorization form

        :param: string
        :param: string
        :return:None
        """
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_PHONE).send_keys(
            login)
        time.sleep(5)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_PASSWORD).send_keys(
            password)
        time.sleep(5)
        self._driver.find_element(*RegistrationAuthorizationPageLocators.LOCATOR_SUBMIT_BUTTON).click()
        time.sleep(5)