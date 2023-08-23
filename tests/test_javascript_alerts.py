from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_javascript_alerts():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()
    # alert.dismiss()

    result_text = driver.find_element(By.XPATH, "//p[normalize-space()='You successfully clicked an alert']")
    print(result_text.text)
