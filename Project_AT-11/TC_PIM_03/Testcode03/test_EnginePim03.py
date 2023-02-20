from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest
from TestData03 import Data03
from TestLocator03 import Locators03

class TestDelete03:
    @pytest.fixture
    def booting_function(self):
        self.driver= webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Employee03(self,booting_function):
        self.driver.get(Data03.PIM_Data03().url)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators03.Pim_Locator03().Username_Locator))).send_keys(Data03.PIM_Data03().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators03.Pim_Locator03().Password_Locator))).send_keys(Data03.PIM_Data03().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators03.Pim_Locator03().LoginButtonLocator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators03.Pim_Locator03().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators03.Pim_Locator03().EmpName_Locator))).send_keys(Data03.PIM_Data03().EmpSearch_Name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators03.Pim_Locator03().Search_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators03.Pim_Locator03().Delete_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators03.Pim_Locator03().YesDelete_Locator))).click()
        sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print('Success : An existing employee has been deleted')