import time
from behave_webdriver.steps import *
from testData.constants import PizzaCheckMessage
from pages.registration_authorization import RegistrationAuthorizationPage
from pages.pizza_page import PizzaPage


# Open maim page
@given('website "{url}"')
def step(context, url):
    context.browser.get(url)

@then("I go to user authorization page")
def step(context):
    context.authorization_page = RegistrationAuthorizationPage(context.browser)
    context.authorization_page.go_to_registration_page()


@then('Login with phone number "{login}" and password "{password}"')
def step(context, login, password):
    context.authorization_page.authorization_form(login, password)
    # time.sleep(5)


# @then('Verify that I registered on website with phone number "{username}"')
# def step(context, username):
#     assert context.authorization_page.get_authorize_user_name() == username


@then('Go to pizza page, add "{product}" to shopping cart and check successful message')
def step(context, product):
    context.pizza_page = PizzaPage(context.browser)
    context.pizza_page.go_to_pizza_page()
    context.pizza_page.generate_product_list()
    context.pizza_page.add_product_to_shopping_cart(product)
    assert context.pizza_page.catch_message() == PizzaCheckMessage.check_message(
        product
    )
    # PizzaPageConstants.SUCCESSFUL_MESSAGE_ITEM_1(product)
