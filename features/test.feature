#noinspection CucumberUndefinedStep
Feature: Check the ability of buying some food for register user on website https://karuzo.ua/

  Scenario: User authorization on website
  Given website "https://karuzo.ua/"
  Then I go to user authorization page
  And Login with username "380672135103" and password "123456"
  #And Verify that I registered on website with username "test10"