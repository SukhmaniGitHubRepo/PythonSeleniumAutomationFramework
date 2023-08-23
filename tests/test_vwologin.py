import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_vwologin():
    logger = logging.getLogger(__name__)
    # Selenium API - Create Session

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open the Browser
    # Navigate to a URL
    # Command - driver.get (Navigate command to Existing Session)
    driver.get("https://app.vwo.com/")

    # Click on the Link Text in the Login Page
    # linktext_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    # linktext_element.click()

    # Find the Email Web element and put email id = "abc@gmail.com
    # Find the Password input box and enter the password =123
    # Click on the button - Sign in
    email_element = driver.find_element(By.ID, "login-username")
    password_element = driver.find_element(By.ID, "login-password")
    sign_in_button_element = driver.find_element(By.ID, "js-login-btn")

    email_element.send_keys("SHAYAM@TTA.COM")
    password_element.send_keys("Wingify@123")
    sign_in_button_element.click()

    time.sleep(5)

    # There is a delay of 2-3 seconds
    logger.info("Just an information")
    assert "Dashboard" in driver.title
