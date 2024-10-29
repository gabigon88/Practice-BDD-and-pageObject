from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
# mobile_emulation = { "deviceName": "iPhone X" } # Specifying device
# options.add_experimental_option("mobileEmulation", mobile_emulation) # For mobile emulation
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False) # Disable Chrome Extension
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10) # 隱性等待，全域影響，最長只等n秒

browser.get("https://www.natural8.com/zh-TW")
wait = WebDriverWait(browser, timeout=10)
wait.until(EC.visibility_of_element_located((By.ID, "home-cta-hero-signupp"))).click()
browser.quit()

# _sign_up_btn_loc = ('By.ID', 'page-link-signup')

# def aaaa(abc):
#     return abc

# def aaa(abc):
#     return abc

# print(aaaa(_sign_up_btn_loc))
# print(aaa(_sign_up_btn_loc))