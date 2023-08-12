# call selenium
# selenium commands

# Selenium Code(Pythin, Java) -> API HTTP Request -> ChromeDriver / Gecko Driver ->  Chrome/Firefox

import pytest
from selenium import webdriver


# Create a Session by API request and navigate to a URL
# If Seleniun < 4,We use to set the driver path
# If Selenium > 4, Driver path is not needed, they will handle automatically

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver  #
    return driver  # the value will be stored permanently, extra variable


def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)
    # Verification
    # Actual Result == ExpectedResult
    assert "Login - VWO" == driver.title
