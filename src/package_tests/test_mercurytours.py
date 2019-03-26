'''
Created on 21-Mar-2019

@author: bhushana
'''
from package_reusables.Reusable_functions import Reusables
import pytest

@pytest.mark.usefixtures("before_function")
class Test_sample:

    reuse = Reusables()

# @pytest.fixture()
# def before_function():
#     print("In Fixture before Yield")
#     reuse.open_browser("Chrome")
#     yield
#     reuse.close_browser()
#     print("In Fixture after Yield")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.repeat(2)
    def test_website(self):
        self.reuse.navigate_to_url(self.driver, "http://newtours.demoaut.com/")
        assert self.reuse.get_title(self.driver)=="Welcome: Mercury Tours"

    @pytest.mark.regression
    def test_registration(self):
        self.reuse.navigate_to_url(self.driver, "http://newtours.demoaut.com/")
        assert self.reuse.get_title(self.driver)=="Welcome: Mercury Tours"
        self.reuse.click_element(self.driver, "//a[text()='REGISTER']", "Register link")
        assert self.reuse.get_title(self.driver)=="Register: Mercury Tours"
        self.reuse.enter_data(self.driver, "//input[@name='firstName']", "Bhushan", "First name")
        self.reuse.enter_data(self.driver, "//input[@name='lastName']", "Bhushan", "Last name")
        self.reuse.enter_data(self.driver, "//input[@name='email']", "Bhushan", "User name")
        self.reuse.enter_data(self.driver, "//input[@name='password']", "Bhushan", "Password")
        self.reuse.enter_data(self.driver, "//input[@name='confirmPassword']", "Bhushan", "Confirm password")
        self.reuse.click_element(self.driver, "//input[@name='register']", "Submit button")
        assert "Thank you for" in self.reuse.get_text(self.driver, "//*[contains(text(),'Thank you for ')]")
 
# @pytest.mark.smoke
# def test_registration1():
#     reuse.navigate_to_url("http://newtours.demoaut.com/")
#     assert reuse.get_title()=="Welcome: Mercury Tours"
#     reuse.click_element("//a[text()='REGISTER']", "Register link")
#     assert reuse.get_title()=="Register: Mercury Tours"
#     reuse.enter_data("//input[@name='firstName']", "Bhushan", "First name")
#     reuse.enter_data("//input[@name='lastName']", "Bhushan", "Last name")
#     reuse.enter_data("//input[@name='email']", "Bhushan", "User name")
#     reuse.enter_data("//input[@name='password']", "Bhushan", "Password")
#     reuse.enter_data("//input[@name='confirmPassword']", "Bhushan", "Confirm password")
#     reuse.click_element("//input[@name='register']", "Submit button")
#     assert "Thank you for" in reuse.get_text("//*[contains(text(),'Thank you for ')]")
#     
# @pytest.mark.smoke
# def test_registration2():
#     reuse.navigate_to_url("http://newtours.demoaut.com/")
#     assert reuse.get_title()=="Welcome: Mercury Tours"
#     reuse.click_element("//a[text()='REGISTER']", "Register link")
#     assert reuse.get_title()=="Register: Mercury Tours"
#     reuse.enter_data("//input[@name='firstName']", "Bhushan", "First name")
#     reuse.enter_data("//input[@name='lastName']", "Bhushan", "Last name")
#     reuse.enter_data("//input[@name='email']", "Bhushan", "User name")
#     reuse.enter_data("//input[@name='password']", "Bhushan", "Password")
#     reuse.enter_data("//input[@name='confirmPassword']", "Bhushan", "Confirm password")
#     reuse.click_element("//input[@name='register']", "Submit button")
#     assert "Thank you for" in reuse.get_text("//*[contains(text(),'Thank you for ')]")
# 
@pytest.mark.smoke
@pytest.mark.progression
def test_links(self):
    self.reuse.navigate_to_url("http://newtours.demoaut.com/")
    assert self.reuse.get_title()=="Welcome: Mercury Tours"
    assert self.reuse.element_presence("//a[text()='Home']", "Home Link")==True
    assert self.reuse.element_presence("//a[text()='Flights']", "Flights Link")==True
    assert self.reuse.element_presence("//a[text()='Hotels']", "Hotels Link")==True
    assert self.reuse.element_presence("//a[text()='Car Rentals']", "Car Rentals Link")==True
    assert self.reuse.element_presence("//a[text()='Cruises']", "Cruises Link")==True
    assert self.reuse.element_presence("//a[text()='Destinations']", "Destinations Link")==True
    assert self.reuse.element_presence("//a[text()='Vacations']", "Vacations Link")==True
    


    
    
    
    
    
    
