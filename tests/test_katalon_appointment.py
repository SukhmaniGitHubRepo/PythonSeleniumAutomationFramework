import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.negative
def test_katalon_appointment_negative():
    # Create a Session by API request
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click on Make Appointment Button
    makeappointmentbutton = driver.find_element(By.ID, "btn-make-appointment")
    makeappointmentbutton.click()

    time.sleep(5)

    username = driver.find_element(By.ID, "txt-username")
    password = driver.find_element(By.ID, "txt-password")

    # Input the Values to the username and password textbox
    username.send_keys("John Cena")
    password.send_keys("ThisIsAPassword")

    # Click on Login Button
    loginbutton = driver.find_element(By.ID, "btn-login")
    loginbutton.click()

    time.sleep(5)

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed!" in error_message.text


@pytest.mark.positive
def test_katalon_appointment():
    # Create a Session by API request
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click on Make Appointment Button
    makeappointmentbutton = driver.find_element(By.ID, "btn-make-appointment")
    makeappointmentbutton.click()

    time.sleep(5)

    username = driver.find_element(By.ID, "txt-username")
    password = driver.find_element(By.ID, "txt-password")

    # Input the Values to the username and password textbox
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")

    # Click on Login Button
    loginbutton = driver.find_element(By.ID, "btn-login")
    loginbutton.click()

    time.sleep(5)

    dropdown = Select(driver.find_element(By.ID, "combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.ID, "radio_program_medicaid").click()

    driver.find_element(By.ID, "txt_visit_date").send_keys("12/12/1991")

    driver.find_element(By.ID, "txt_comment").send_keys("General Checkup")

    driver.find_element(By.ID, "btn-book-appointment").click()

    time.sleep(5)

    # Verify Appointment Confirmation

    appointment_confirmation_text = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in appointment_confirmation_text.text
