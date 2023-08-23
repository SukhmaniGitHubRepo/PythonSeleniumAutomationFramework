import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_javascript_checkboxes():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/checkboxes")

    javascript_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    # Check the Checkboxes which is not selected
    for c in javascript_checkboxes:
        if not c.is_selected():
            c.click()

            time.sleep(10)
