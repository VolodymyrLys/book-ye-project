from behave_webdriver.steps import *
from pages.registration_authorization import RegistrationAuthorizationPage
#from testData.constants import *


# Open maim page
@given('website "{url}"')
def step(context, url):
    context.browser.get(url)


@then('I go to user authorization page')
def step(context):
    context.authorization_page = RegistrationAuthorizationPage(context.browser)
    context.authorization_page.go_to_registration_page()


@then('Login with username "{login}" and password "{password}"')
def step(context, login, password):
    context.authorization_page.authorization_form(login, password)


@then('Verify that I registered on website with username "{username}"')
def step(context, username):
    assert context.authorization_page.get_authorize_user_name() == username
