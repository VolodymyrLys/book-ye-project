from selenium.webdriver.common.by import By


class PizzaPageLocators:
    """Locators for Pizza Page."""

    #LOCATOR_PRODUCTS = (By.XPATH, "//div[@id='product_15']")
    LOCATOR_PRODUCTS = (By.XPATH, "//div[@class='goods-element']")
    LOCATOR_PRODUCT_NAME = (By.XPATH, "/a/h2")
    LOCATOR_ADD_TO_CART = (By.XPATH, "div/div/div[@class='recentCart']/div[@class='variable-price-wrap']/a")
    LOCATOR_MESSAGE_ADD_TO_CART = (By.CLASS_NAME, "message_cart")