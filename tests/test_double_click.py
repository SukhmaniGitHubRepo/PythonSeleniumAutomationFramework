import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_double_click():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    clickable = driver.find_element(By.ID, "clickable")

    ActionChains(driver) \
        .double_click(clickable) \
        .perform()

    time.sleep(10)
