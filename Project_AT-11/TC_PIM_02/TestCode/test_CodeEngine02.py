from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import pytest
from TestLocator import Locators02
from TestData import Data02

class TestOrange:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,30)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_PIM_02(self, booting_function):
        self.driver.get(Data02.PIM_Data.url)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators02.PIM_Locators().Username_locator))).send_keys(Data02.PIM_Data().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME, Locators02.PIM_Locators().Password_Locator))).send_keys(Data02.PIM_Data().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().LoginButtonLocator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().EmpName_Locator))).send_keys(Data02.PIM_Data().EmpSearch_Name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().Search_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().Edit_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().Nick_Locator))).send_keys(Data02.PIM_Data().NickName)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().OtherID_Locator))).send_keys(Data02.PIM_Data().Other_ID)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().LiceNO_Locator))).send_keys(Data02.PIM_Data().Licen_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().LexDate_Locator))).send_keys(Data02.PIM_Data().LiEX_Date)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().SSN_Locator))).send_keys(Data02.PIM_Data().SSN_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().SIN_Locator))).send_keys(Data02.PIM_Data().SIN_NO)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().DOB_Locator))).send_keys(Data02.PIM_Data().DOB)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().Gender_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().Military_Locator))).send_keys(Data02.PIM_Data().Military)
        self.wait.until(EC.presence_of_element_located((By.XPATH, Locators02.PIM_Locators().Save_Locator))).click()
        sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print('Success : Existing employee has been edited')