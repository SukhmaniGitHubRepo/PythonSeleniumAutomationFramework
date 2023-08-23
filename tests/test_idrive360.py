import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_idrive360():
    # Create a Session by API request
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.XPATH, "//input[@id ='username']")
    password = driver.find_element(By.XPATH, "//input[@id='password']")

    username.send_keys("augtest_100823@idrive.com")
    password.send_keys("123456")

    sign_in_button = driver.find_element(By.XPATH, "//button[text()='Sign in']")
    sign_in_button.click()

    time.sleep(15)

    # Click on "+ Add Devices"
    driver.find_element(By.XPATH, "//a[@id='add-device-header-btn']").click()

    time.sleep(10)

    # Click on Mac Tab
    driver.find_element(By.XPATH, "//a[@id='add-device-mac-tab']").click()

    time.sleep(10)
    # Click on Download Backup Agent
    driver.find_element(By.XPATH, "//div[@id='id-card-bdy-backup-agent-mac']/button").click()

    time.sleep(10)
