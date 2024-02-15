#noinspection CucumberUndefinedStep
Feature: Check the ability of buying some food for register user on website https://karuzo.ua/

#  Scenario: User authorization on website
#  Given website "https://karuzo.ua/"
#  Then I go to user authorization page
#  And Login with phone number "0672135103" and password "123456"
#  #And Verify that I registered on website with phone number "0672135103"

  Scenario: Login on website and add pizza to cart
  Given website "https://karuzo.ua/"
  Then I go to user authorization page
  And Login with phone number "0672135103" and password "123456"
  #And Verify that I registered on website with username "0672135103"
  And Go to pizza page, add "ПІЦА ЖИРНИЙ ФРАЄР" to shopping cart and check successful message