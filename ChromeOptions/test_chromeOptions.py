from selenium import webdriver


# Chrome -> Chrome Options
# Chrome Options - Chrome with the Extension, Window Size, Proxy, JS disabled

def test_login():
    chrome_options = webdriver.ChromeOptions()

    # Chrome Options can also be used to add Extensions to the Chrome Browser While running
    # Suppose extension has been downloaded into Download, then path will be as mentioned below:
    # extension_path = "/Users/Sukhmani/Downloads/adblocker.crx"

    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_extension(extension_path)

    # 1. Headless mode: Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--headless=new")

    # With UI - slow and consume lot of resource, You can see the Test - 100 TC's
    # Without UI - headless - fast, it will consume less resource, You can't see the test - 1000 TC's

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/")
