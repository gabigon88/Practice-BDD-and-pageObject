from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, _driver: webdriver):
        self.driver = _driver
        self.wait = WebDriverWait(_driver, 10)

    def get(self, url):
        self.driver.get(url)

    def close(self):
        ''' 關閉當前的視窗，其他的仍然保持打開狀態，如果只打開了一個視窗，那會關閉整個瀏覽器。 '''
        self.driver.close()
    
    def quit(self):
        ''' 關閉所有與 WebDriver 相關的視窗，並且完全終止瀏覽器的進程。 '''
        self.driver.quit()

    def find_element(self, loc):
        return self.wait.until(EC.visibility_of_element_located(loc))

    def find_elements(self, loc):
        self.wait.until(EC.visibility_of_element_located(loc))
        return self.driver.find_elements(loc)

    def wait_for_alert(self):
        try:
            alert = self.driver.find_element(By.XPATH, '//*[@role="alert"]')
            self.wait.until(EC.staleness_of(alert))
        except:
            pass
        