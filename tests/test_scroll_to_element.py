import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_double_click():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME, "iframe")

    ActionChains(driver) \
        .scroll_to_element(iframe) \
        .perform()

    time.sleep(10)
