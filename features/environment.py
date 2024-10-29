import os
import datetime
import re
from selenium import webdriver
from behave.log_capture import capture

FAILED_SCREENSHOT_DIR_PATH = "./failed_screenshots/"

@capture
def before_all(context):
    if not os.path.exists(FAILED_SCREENSHOT_DIR_PATH):
        os.makedirs(FAILED_SCREENSHOT_DIR_PATH)

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--auto-open-devtools-for-tabs")
    mobile_emulation = { "deviceName": "iPhone X" } # Specifying device
    options.add_experimental_option("mobileEmulation", mobile_emulation) # For mobile emulation
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False) # Disable Chrome Extension
    context.browser = webdriver.Chrome(options=options)
    context.browser.implicitly_wait(10) # 隱性等待，全域影響，最長只等n秒
    
def after_scenario(context, scenario):
    context.browser.quit()

@capture
def after_step(context, step):
    if step.status == 'failed':
        # 用正規表示法, 把檔名不能使用的特殊字元換成 "-"
        fileName = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S_') + re.sub(r":|\/", "-", step.name) + "_failed.png"
        context.browser.save_screenshot(FAILED_SCREENSHOT_DIR_PATH + fileName)