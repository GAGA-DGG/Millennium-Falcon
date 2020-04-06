import time

import click
import self
import pytest
from pip import __init__
from selenium import webdriver
# from selenium.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait





class button():

    def find_button(self):
        self.find_button = webdriver.Chrome.find_element_by_css_selector()
    # def click_button(self):
        # self.click_button =

    #         # self.push = push
    #


#
#     # def push(self):
#     #     .click
#
#     def send_key(self, param):
#         pass


options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.fullscreen_window()
driver.implicitly_wait(2)
driver.get("http://www.planetfor.me")

# button.find_button(".search-input").send_key("gfhfsk")

# @pytest.fixture
# def open_chrome():
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=options)
#     driver.fullscreen_window()


# def test_open_chrome.driver.get("http://www.pfm.ru"):

# driver.get("http://www.pfm.ru")
#
# open_chrome(a)
#
#
# class Web_element:
#     classmethod
#     find = driver.find_element_by_css_selector()
#
#
#
# Web_element.find(".search-input")
# # Web_element.find(".search-input")
# # ddd.click("paark")
# # Web_element.click()
pfmSearch = driver.find_element_by_css_selector(".search-input")
# time.sleep(2)
# # pfmSearch.send_keys("djfsak;faks;dbv")
pfmSearch.send_keys("аквапарк")
# time.sleep(2)
submit_button = driver.find_element_by_css_selector(".search-item").click()
# time.sleep(2)
# submit_button.click()
# # time.sleep(2)
submit_button = driver.find_element_by_css_selector(".sphere-300").click()
# time.sleep(2)
# submit_button.click()
# # time.sleep(2)
submit_button = driver.find_element_by_css_selector(".popup_slider_circle_counter_right_arrow").click()
# time.sleep(1)
# submit_button.click()
# # time.sleep(1)
submit_button = driver.find_element_by_css_selector(".popup_slider_circle_counter_right_arrow")
# time.sleep(1)
submit_button.click()
# time.sleep(1)
submit_button = driver.find_element_by_css_selector(".popup_slider_circle_counter_right_arrow")
# time.sleep(1)
submit_button.click()
# time.sleep(1)
# submit_button = driver.find_element_by_css_selector(".popup_slider_circle_counter_right_arrow")
# time.sleep(1)
# submit_button.click()
# time.sleep(1)
# submit_button = driver.find_element_by_css_selector(".popup_slider_circle_counter_left_arrow")
# time.sleep(1)
# submit_button.click()
# time.sleep(1)
# submit_button = driver.find_element_by_css_selector(".popup_slider_circle_counter_left_arrow")
# time.sleep(1)
# submit_button.click()
# time.sleep(1)
# submit_button = driver.find_element_by_css_selector(".popup_slider_circle_counter_left_arrow")
# time.sleep(1)
# submit_button.click()
# time.sleep(1)
# submit_button = driver.find_element_by_css_selector(".popup_slider_close")
# time.sleep(1)
# submit_button.click()
# time.sleep(1)
# submit_button = driver.find_element_by_css_selector(".glow-64-toned")
# time.sleep(1)
# submit_button.click()
# time.sleep(2)

# submit_button = driver.find_element_by_css_selector("icon-dots > path:nth-child(1)")
# time.sleep(1)
# submit_button.click()
# time.sleep(1)
# target = driver.find_element_by_link_text("Сорочаны")
# target.location_once_scrolled_into_view
# time.sleep(1)
# submit_button = driver.find_element_by_css_selector("article.sphere-container:nth-child(8) > a:nth-child(1) > div:nth-child(1)")
# time.sleep(1)
# submit_button.click()
# time.sleep(1)
# parent_h = driver.current_window_handle
# checkIn = driver.find_element_by_id('qaCheckin_anchor')
# submit_button.click()

# submit_button = driver.find_element_by_css_selector()
# time.sleep(2)
# submit_button.click()
# time.sleep(2)
# submit_button = driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/span[4]")
# time.sleep(2)
#
# driver.quit()
# 1.сlass
# 2.metods
# 3.trycatch
# 4.search error
# 5.selenium tests
# 6.logs
# 7. 6,7,8
# 8.pylind

