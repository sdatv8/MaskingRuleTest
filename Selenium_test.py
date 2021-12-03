# import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from DataBaseConnect import PostgreSelect
from MaskingRule import PostgresMaskingRule
from CheckMaskingTable import CheckMasking

class TestMaskingRule():

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('ignore-certificate-errors')
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def ConnectDS(self):
        driver = self.driver
        driver.maximize_window()
        try:
            driver.get('https://192.168.10.108:11000/v2')
            connect = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginSubmit"]/button')))
            loginUser = driver.find_elements_by_class_name('input__control')[0].send_keys('admin')
            loginPass = driver.find_elements_by_class_name('input__control')[1].send_keys('')
            logIn = driver.find_element_by_class_name('MuiButton-label').click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/nav/div/div[1]/ul/li[11]/button')))
        except:
            print("Error connect!")

    def CreateInstance(self):
        driver = self.driver
        GoDataBase = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/nav/div/div/ul/li[11]/button').click()
        add_instance = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/a/button').click()
        PostgreSelect(driver)

    def CreateMaskingRule(self):
        driver = self.driver
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/nav/div/div[1]/ul/li[5]/button/span[2]'))).click()
            DynamicMasking = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/nav/div/div[1]/ul/li[5]/ul[2]/li[1]/a').click()
            NewMasking = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a').click()
            PostgresMaskingRule(driver)
        except:
            print('Error create masking rules!')

    def MaskingCheck(self):
        test = CheckMasking()
        if (test == 10):
            print('Masking SUCCESS!')
        elif (test == -1):
            print('Error database connect!')
        else:
            print('Error MASKING!')

    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    test = TestMaskingRule()
    try:
        test.ConnectDS()
        test.CreateInstance()
        time.sleep(10)
        test.CreateMaskingRule()
        test.TearDown()
        time.sleep(10)
        test.MaskingCheck()
    except:
        test.TearDown()
