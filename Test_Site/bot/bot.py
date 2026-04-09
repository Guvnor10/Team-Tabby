import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "http://proxy"
TRIGGER_FILE = "/bot/start_bot"

def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

def simulate_user():
    driver = create_driver()
    try:
        driver.get(URL)
        time.sleep(random.uniform(2,5))
        links = driver.find_elements("tag name", "a")
        if links:
            random.choice(links).click()
            time.sleep(random.uniform(2,5))
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

def run_bot():
    print(f"Waiting for trigger file {TRIGGER_FILE} to start traffic...")
    while True:
        if os.path.exists(TRIGGER_FILE):
            print("Trigger detected, running bot...")
            simulate_user()
            time.sleep(random.uniform(5,15))
        else:
            print("Trigger file missing, bot paused. Waiting...")
            time.sleep(1)

if __name__ == "__main__":
    run_bot()