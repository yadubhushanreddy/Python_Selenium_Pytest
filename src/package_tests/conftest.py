'''
Created on 25-Mar-2019

@author: bhushana
'''
import pytest
from package_reusables.Reusable_functions import Reusables

reuse = Reusables()

@pytest.fixture()
def before_function(request):
    driver = reuse.open_browser("Chrome")
    request.cls.driver = driver
    yield
    reuse.close_browser(driver)
    
