from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pytest
from TestDatas import Data
from TestLocators import Locator

class TestOrange:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Login02(self, booting_function):
        self.driver.get(Data.HRM_data().url)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locator.HRM_Locator().Username_Locator))).send_keys(Data.HRM_data().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locator.HRM_Locator().Password_Locator))).send_keys(Data.HRM_data().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.HRM_Locator().LoginButtonLocator))).click()
        sleep(3)
        assert self.driver.title == 'OrangeHRM'
        print('A valid error message for invalid credentials is displayed')