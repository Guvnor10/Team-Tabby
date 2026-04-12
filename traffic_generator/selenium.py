import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

MEALIE_URL = "http://proxy"
TRIGGER_FILE = "/traffic_generator/generating_traffic"

def new_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def the_user():
    driver = new_driver()
    try:
        driver.get(MEALIE_URL)
        time.sleep(random.uniform(2,5))
        links = driver.find_elements("tag name", "a")
        if links:
            random.choice(links).click()
            time.sleep(random.uniform(2,5))
    except Exception as ex:
        print("Error:", ex)
    finally:
        driver.quit()

def run_traffic_generator():
    print(f"Waiting for trigger file {TRIGGER_FILE} to start traffic...")
    while True:
        if os.path.exists(TRIGGER_FILE):
            print("Trigger detected, please proceed with the traffic generation.")
            the_user()
            time.sleep(random.uniform(9,29))
        else:
            print("Trigger file missing, please wait until it is found.")
            time.sleep(1)

if __name__ == "__main__":
    run_traffic_generator()