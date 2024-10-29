import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pageObject.LoginPage import LoginPage
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# given-----------------------------------------------
@given('I open login page')
def step_impl(context):
    context.login_page = LoginPage(context.browser)


# when-----------------------------------------------
@when('I click sign up link')
def step_impl(context):
    context.login_page.click_sign_up()

@when('I click forgot password')
def step_impl(context):
    context.login_page.click_forgot_password()

@when('I swtich to phone-login')
def step_impl(context):
    context.login_page.switch_to_phone_login()

@when('I input {email} in email field')
def step_impl(context, email):
    context.login_page.input_email(email)

@when('I input {password} in password field')
def step_impl(context, password):
    context.login_page.input_password(password)

@when('I click login button')
def step_impl(context):
    context.login_page.click_login()

# then-----------------------------------------------
# @then('page is sign up page')
# def step_impl(context):
#     assert context.browser.current_url == "https://www.natural8.com/zh-TW/sign-up"

@then('page is forgot password page')
def step_impl(context):
    sleep(1) # 頁面會有跳轉, 所以稍等一下
    assert "https://fp.cashier-natural8.com/app/find-pw" in context.browser.current_url

@then('account field is phone field')
def step_impl(context):
    assert context.login_page.find_element(context.login_page._phone_type_loc).is_displayed()

@then('userName is {account}')
def step_impl(context, account):
    assert context.login_page.find_element(context.login_page._login_btn_loc).text == "在登錄..."

