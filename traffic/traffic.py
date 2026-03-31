import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SELENIUM_URL = os.getenv("SELENIUM_URL", "http://selenium:4444")
TARGET_URL = os.getenv("TARGET_URL", "http://proxy")

def run():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    print(f"Connecting to Selenium at {SELENIUM_URL}")
    driver = webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=options
    )

    try:
        for i in range(5):
            print(f"Visit #{i+1}")

            driver.get(TARGET_URL)
            time.sleep(5) 

            driver.get(TARGET_URL + "/recipes")
            time.sleep(5)

            driver.refresh()
            time.sleep(3)

        print("Traffic generation complete.")

    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    run()