import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver(request):
    # wd=webdriver.firefox(firefox_binary="

    capabilities = DesiredCapabilities.CHROME
    wd = webdriver.Chrome('/Users/dengarbuzov/Documents/browser drivers')
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://planetfor.me/Rv5W03j")
    # driver.get("https://otus.ru/")