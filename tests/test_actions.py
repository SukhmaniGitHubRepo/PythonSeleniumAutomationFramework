import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def test_actions():
    driver = webdriver.Chrome()
    driver.get("http://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.NAME, "firstname")

    # Create Object of Action Chains Class
    actions = ActionChains(driver)
    # Send Keys but with the Shift
    # Press Shift Key Down
    # Press Shift Key Up (release)
    actions.key_down(Keys.SHIFT). \
        send_keys_to_element(first_name, "the testing academy") \
        .key_up(Keys.SHIFT).perform()  # press shift key up (release)

    time.sleep(20)

    # Right Click on the Link (Using Context Click)
    download_link = driver.find_element(By.XPATH, "//a[text()='Click here to Download File']")
    actions.context_click(download_link).perform()
    time.sleep(10)

    # If Focus/Mouse Cursor is there on the element, we can use sendkeys directly
    # whereas if the focus.mouse cursor is out of focus, we can use
    # actions.key_down(Keys.SHIFT). \
    #         send_keys_to_element(first_name, "the testing academy") \
    #         .key_up(Keys.SHIFT).perform()  # press shift key up (release)





