from .BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class HomePage(BasePage):
    _headerMenu_loc = (By.ID, 'header-button-mobile-open-btn')
    _sign_up_btn_loc = (By.ID, 'home-cta-hero-mobile-signup')
    _login_btn_loc = (By.ID, 'header-cta-mobile-login')
    _download_btn_loc = (By.ID, 'header-cta-mobile-download')

    def __init__(self, _driver):
        super(HomePage, self).__init__(_driver)
        self.driver.get("https://www.natural8.com/zh-TW")

    def open_menu(self):
        self.find_element(self._headerMenu_loc).click()
    
    def click_sign_up_page(self):
        self.find_element(self._sign_up_btn_loc).click()
    
    def click_login_page(self):
        self.find_element(self._login_btn_loc).click()
    
    def click_download_page(self):
        self.find_element(self._download_btn_loc).click()
    