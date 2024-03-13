from selenium.webdriver.common.by import By


class PizzaPageLocators:
    """Locators for Pizza Page."""

    # LOCATOR_PRODUCTS = (By.XPATH, "//div[@id='product_15']")
    LOCATOR_PRODUCTS = (By.XPATH, "//div[@class='goods-element']")
    LOCATOR_PRODUCT_NAME = (By.XPATH, "a/h2")
    LOCATOR_ADD_TO_CART = (
        By.XPATH,
        "div[@class='set-goods']/a[@class='goods-cart goods-cart_category']",
    )
    LOCATOR_MESSAGE_ADD_TO_CART = (By.XPATH, "//div[@id='ohsnap']/div")
