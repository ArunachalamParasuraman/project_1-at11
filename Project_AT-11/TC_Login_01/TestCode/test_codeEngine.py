from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from TestData import Data
from TestLocators import Locator


class TestOrange:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Login(self, booting_function):
        self.driver.get(Data.HRM_Data().url)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locator.HRM_Locator().Username_Locator))).send_keys(Data.HRM_Data().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locator.HRM_Locator().Password_Locator))).send_keys(Data.HRM_Data().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.HRM_Locator().LoginButtonLocator))).click()
        assert self.driver.title == 'OrangeHRM'
        print('The user is logged in successfully')

