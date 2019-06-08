'''
Created on 21-Mar-2019

@author: bhushana
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Reusables:
    

    
    def __init__(self):
        pass
    
    def open_browser(self, browser_name):
        try:
            if browser_name == 'Chrome':
                #driver = webdriver.Chrome(executable_path = '/Users/bhushana/Downloads/chromedriver')
                driver = webdriver.Remote(command_executor='http://192.168.1.4:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
                driver.maximize_window()
                print("Chrome browser opened")
                return driver
        except:
            print("Opening Chrome Browser failed")
            return None
            
    def navigate_to_url(self, driver, url):
        driver.get(url)
        print("Navigated to "+url)
        
    def wait_for_element(self, driver, test_object):
        wait = WebDriverWait(driver, 30)
        return wait.until(EC.presence_of_element_located((By.XPATH, test_object)))
    
    def click_element(self, driver, test_object, element_desc):
        try:
            self.wait_for_element(driver, test_object).click()
            print("Clicking on '"+element_desc+"' Successful")
        except:
            print("Failed in Click method")
            
    def element_presence(self, driver, test_object, element_desc):
        exists = self.wait_for_element(driver, test_object).is_displayed()
        print(element_desc+" was displayed")
        return exists
        
    def enter_data(self, driver, test_object, test_data, element_desc):
        self.wait_for_element(driver, test_object).send_keys(test_data)
        print("Entering "+test_data+" in '"+element_desc+"' Successful")
        
    def get_text(self, driver, test_object):
        return self.wait_for_element(driver, test_object).text
    
    def get_title(self, driver):
        return driver.title
    
    def close_browser(self, driver):
        driver.quit()
        print("Browser Closed")
