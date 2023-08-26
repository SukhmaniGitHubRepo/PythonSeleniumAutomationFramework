import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_double_click():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    hovered = driver.find_element(By.ID, "hover")

    ActionChains(driver) \
        .move_to_element(hovered) \
        .perform()

    time.sleep(10)
