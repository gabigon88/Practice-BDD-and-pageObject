from .BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):
    _sign_up_btn_loc = (By.ID, 'page-link-signup')
    _forgot_btn_loc = (By.ID, 'page-link-forgot-password')
    _email_type_loc = (By.XPATH, '//label[@for="email-login-type"]')
    _phone_type_loc = (By.XPATH, '//label[@for="phone-login-type"]')
    _emailTF_loc = (By.XPATH, '//input[@name="email"]')
    _phoneTF_loc = (By.XPATH, '//input[@name="phone"]')
    _passwordTF_loc = (By.XPATH, '//input[@name="password"]')
    _login_btn_loc = (By.ID, 'login-button')   

    def __init__(self, _driver):
        super(LoginPage, self).__init__(_driver)
        self.driver.get("https://www.natural8.com/zh-TW/login")

    def click_sign_up(self):
        self.find_element(self._sign_up_btn_loc).click()

    def click_forgot_password(self):
        self.find_element(self._forgot_btn_loc).click()
    
    def switch_to_email_login(self):
        self.find_element(self._email_type_loc).click()

    def switch_to_phone_login(self):
        self.find_element(self._phone_type_loc).click()

    def input_email(self, account):
        self.find_element(self._emailTF_loc).clear()
        self.find_element(self._emailTF_loc).send_keys(account)

    def input_phone(self, account):
        self.find_element(self._phoneTF_loc).clear()
        self.find_element(self._phoneTF_loc).send_keys(account)

    def input_password(self, password):
        self.find_element(self._passwordTF_loc).clear()
        self.find_element(self._passwordTF_loc).send_keys(password)

    def click_login(self):
        self.find_element(self._login_btn_loc).click()