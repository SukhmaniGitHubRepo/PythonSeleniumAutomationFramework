import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


def test_double_click():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME, "iframe")

    scroll_origin = ScrollOrigin.from_element(iframe)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    time.sleep(10)
