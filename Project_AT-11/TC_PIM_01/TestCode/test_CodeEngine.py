from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pytest
from TestLocator import Locators
from TestData import Data

class TestOrange:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,30)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_PIM_01(self, booting_function):
        self.driver.get(Data.HRM_Data().url)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.HRM_Locator().Username_locator))).send_keys(Data.HRM_Data().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.HRM_Locator().Password_Locator))).send_keys(Data.HRM_Data().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().LoginButtonLocator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().Add_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.HRM_Locator().FName_Locator))).send_keys(Data.HRM_Data().FirstName)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.HRM_Locator().MName_Locator))).send_keys(Data.HRM_Data().MiddleName)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators.HRM_Locator().LName_Locator))).send_keys(Data.HRM_Data().LastName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().ID_Locator))).send_keys(Data.HRM_Data().EmployeeID)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().LogDetail_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().LogUser_Locator))).send_keys(Data.HRM_Data().LogUsername)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().LogPass_Locator))).send_keys(Data.HRM_Data().LogPassword)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().LogConPass_Locator))).send_keys(Data.HRM_Data().LogPassword)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.HRM_Locator().Save_Locator))).click()
        sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print('Success : A New Employee has been added')


