from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By


def test_action_builder():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Click - Normal and action will performed
    # Click and Hold - click and hold -> click but will not release

    driver.find_element(By.ID, "click").click()

    # Action Builder ->Mouse - Back

    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.pointer_action.pointer_up(MouseButton.BACK)
    actions_builder.perform()
