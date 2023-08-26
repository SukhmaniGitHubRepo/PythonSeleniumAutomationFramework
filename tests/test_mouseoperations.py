import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def test_actions():
    driver = webdriver.Chrome()
    driver.get("http://awesomeqa.com/selenium/mouse_interaction.html")
    clickable = driver.find_element(By.ID, "clickable")
    actions = ActionChains(driver)
    actions.click_and_hold(clickable).key_down(Keys.SHIFT).key_down("A").perform()

    time.sleep(10)

    # Click - Normal and action will performed
    # Click and Hold - click and hold -> click but will not release
    clickable_link = driver.find_element(By.ID, "click")
    ActionChains(driver) \
        .click_and_hold(clickable_link) \
        .perform()

    assert "resultPage.html" in driver.current_url

    time.sleep(15)
