from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables_static():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")

    # Row
    # // table[contains( @ id, "cust")] / tbody / tr
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@ id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    # Col
    # //table[contains(@id, "cust")]/tbody/tr[2]/td
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@ id,'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    first_part = "//table[contains(@ id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(2, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            # print(data.text, end=" ")

            # Find Helen Bennett Country
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennett is in {country_text}")


def test_web_tables_dynamic():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']")
    row_table = table.find_elements(By.TAG_NAME, "tr") # //table[@summary='Sample Table']/tbody/tr[4]/td

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)

