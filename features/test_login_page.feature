# https://stackoverflow.com/questions/40763066/how-to-generate-reports-in-behave-python

Feature: Test login page

  Scenario: click sign up link
    Given I open login page
    When I click sign up link
    Then page is sign up page

  Scenario: click forgot password
    Given I open login page
    When I click forgot password
    Then page is forgot password page

  Scenario: switch login type
    Given I open login page
    When I swtich to phone-login
    Then account field is phone field
  
  Scenario Outline: user login
    Given I open login page
    When I input <email> in email field
    When I input <password> in password field
    When I click login button
    Then userName is <email>

    Examples:
      | email               | password   |
      | ggwp12345@gmail.com | abcde12345 |