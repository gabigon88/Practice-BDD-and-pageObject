import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pageObject.HomePage import HomePage
from behave import given, when, then
from time import sleep

# given-----------------------------------------------
@given('I open home page')
def step_impl(context):
    context.home_page = HomePage(context.browser)


# when-----------------------------------------------
@when('I click sign up button')
def step_impl(context):
    context.home_page.click_sign_up_page()

@when('I open header meum')
def step_impl(context):
    context.home_page.open_menu()
    sleep(1) # 等待header menu展開動畫
    
@when('I click go to login page')
def step_impl(context):
    context.home_page.click_login_page()

@when('I click go to download page')
def step_impl(context):
    context.home_page.click_download_page()

# then-----------------------------------------------
@then('page is sign up page')
def step_impl(context):
    assert context.browser.current_url == "https://www.natural8.com/zh-TW/sign-up"

@then('page is login page')
def step_impl(context):
    assert context.browser.current_url == "https://www.natural8.com/zh-TW/login"

@then('page is download page')
def step_impl(context):
    assert context.browser.current_url == "https://www.natural8.com/zh-TW/download"

