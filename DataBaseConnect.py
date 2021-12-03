import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def PostgreSelect(driver):
    xPath  = driver.find_element_by_xpath
    cName = driver.find_element_by_class_name
    try:
        DataBaseType = cName('Select-value').click()
        DataBaseType = xPath("//*[contains(@class, 'Select-menu-outer')]//*[text() = 'PostgreSQL']").click()
        HostNameIp = xPath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[3]/div/div/input').send_keys('192.168.1.244')
        Port = xPath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[4]/div/div/input')
        Port.send_keys('\b\b\b\b')
        Port.send_keys('5436')
        DefaultLogin = xPath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[6]/div/div/input').send_keys('postgres')
        PasswordSet = xPath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[8]/div/div/input').send_keys('1234')
        SavePassword = xPath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[7]/div/div/div/div/div/div/div[1]').click()
        SavePassword = xPath("//*[contains(@class, 'Select-menu-outer')]//*[text() = 'Save in ']").click()
        DataBase = xPath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[9]/div/div/input').click()
        # DataBase.clear()
        # DataBase.send_keys('postgres')
        TestConnection = xPath('//*[@id="root"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[4]/span/button/span[1]').click()
        time.sleep(2)
        SaveInstance = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/span/button/span[1]'))).click()
        # time.sleep(2)
        # SaveInstance = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div/span/button/span[1]').click()
    except:
        print('Error connect base!')