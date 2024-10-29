# https://stackoverflow.com/questions/40763066/how-to-generate-reports-in-behave-python

Feature: Test home page

  Scenario: click sign up link
    Given I open home page
    When I click sign up button
    Then page is sign up page

  Scenario: click forgot password
    Given I open home page
    When I open header meum
    When I click go to login page
    Then page is login page

  Scenario: switch login type
    Given I open home page
    When I open header meum
    When I click go to download page
    Then page is download page
