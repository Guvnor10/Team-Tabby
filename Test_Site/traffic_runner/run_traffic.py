import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException

TARGET_URL = "http://proxy"
TOTAL_VISITS = 5
START_DELAY = 10


def build_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)


def open_main_page(driver, visit_number):
    print(f"Visit {visit_number}: opening the site")
    driver.get(TARGET_URL)
    time.sleep(random.uniform(2, 4))
    print(f"Visit {visit_number}: landed on {driver.current_url}")


def collect_links(driver):
    found_links = driver.find_elements("tag name", "a")
    usable_links = []

    for link in found_links:
        try:
            text = link.text.strip()
            href = link.get_attribute("href")
            if text or href:
                usable_links.append(link)
        except Exception:
            continue

    return usable_links


def click_links(driver, visit_number):
    links = collect_links(driver)

    if not links:
        print(f"Visit {visit_number}: no usable links showed up")
        return

    random.shuffle(links)
    number_to_try = min(2, len(links))

    for index in range(number_to_try):
        try:
            link = links[index]
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            time.sleep(1)
            link.click()
            print(f"Visit {visit_number}: clicked link {index + 1}")
            time.sleep(random.uniform(2, 4))
            driver.back()
            time.sleep(random.uniform(2, 3))
        except StaleElementReferenceException:
            print(f"Visit {visit_number}: the page changed before the next click, so I skipped that one")
        except Exception as error:
            print(f"Visit {visit_number}: ran into a click error: {error}")


def run_one_visit(visit_number):
    driver = build_driver()

    try:
        open_main_page(driver, visit_number)
        click_links(driver, visit_number)
        print(f"Visit {visit_number}: done")
    except Exception as error:
        print(f"Visit {visit_number}: something went wrong: {error}")
    finally:
        driver.quit()
        print(f"Visit {visit_number}: browser closed")


def main():
    print("Starting traffic runner")
    print(f"Target: {TARGET_URL}")
    print(f"Planned visits: {TOTAL_VISITS}")
    print(f"Waiting {START_DELAY} seconds so the site can finish loading")

    time.sleep(START_DELAY)

    for visit_number in range(1, TOTAL_VISITS + 1):
        run_one_visit(visit_number)
        time.sleep(random.uniform(3, 6))

    print("Traffic runner finished")


if __name__ == "__main__":
    main()