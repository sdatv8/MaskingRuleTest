import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def PostgresMaskingRule(driver):
    SelectInstance = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div/div/div/div[1]/span').click()
    SelectInstance = driver.find_element_by_xpath("//*[contains(@class, 'Select-menu-outer')]//*[text() = 'PostgreSQL@192.168.1.244:5436']").click()
    time.sleep(3)
    AddTable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[5]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/button')))
    AddTable = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[5]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/button').click()
    Selectbase = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[8]/div/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div[13]/div/div/div/div[1]/div[1]/button'))).click()
    SelectSchema = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[8]/div/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div[18]/div/div/div/div[1]/div[1]/button'))).click()
    time.sleep(1)
    SelectTable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[8]/div/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div[19]/div/div/div/div[1]/div[1]/button'))).click()
    time.sleep(1)
    SelectColumn_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[8]/div/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div[21]/div/div/div/div[1]/div[1]'))).click()
    SelectColumn_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[8]/div/div/div[2]/div/div[2]/div[4]/div[2]/div/div/div[22]/div/div/div/div[1]/div[1]'))).click()
    time.sleep(1)
    SaveMatch = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[8]/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/span/button'))).click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[5]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]').click()
    driver.find_element_by_xpath("//*[contains(@class, 'Select-menu-outer')]//*[text() = 'Mask first chars']").click()
    time.sleep(1)
    CharcterCount = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[5]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div/div/input')
    CharcterCount.send_keys('\b')
    CharcterCount.send_keys('2')
    time.sleep(1)
    save = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[6]/div/div/div[2]/span[2]/button').click()