import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_make_my_trip():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    time.sleep(5)

    from_city = driver.find_element(By.ID, "fromCity")

    actions = ActionChains(driver)
    actions.move_to_element(from_city).click().send_keys("CHD").perform()
    time.sleep(10)
