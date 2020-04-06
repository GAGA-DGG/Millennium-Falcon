
import time

from selenium import webdriver
def test_one():
 options = webdriver.ChromeOptions()
 options.add_argument("--kiosk")
 driver = webdriver.Chrome(options=options)
 driver.get("https://planetfor.me")
 time.sleep(2)
 pfmSearch = driver.find_element_by_css_selector(".search-input")
 time.sleep(2)
 pfmSearch.send_keys("шаурма")
 time.sleep(2)
 submit_button = driver.find_element_by_css_selector(".search-item")
 time.sleep(2)
 submit_button.click()
 time.sleep(3)
 driver.quit()