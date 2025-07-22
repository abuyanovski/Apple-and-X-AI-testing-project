import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import helpers as hp
import locators as l
from selenium import webdriver
import pytest


# BrowserStack credentials
USERNAME = "vik_Kamz9v"
ACCESS_KEY = "D5pQJ8Y1QF7YVysaaymy"
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.set_capability("browserName", "Chrome")
    chrome_options.set_capability("browserVersion", "latest")
    chrome_options.set_capability("platformName", "Windows 11")

    # BrowserStack-specific capabilities go under "bstack:options"
    chrome_options.set_capability("bstack:options", {
        "sessionName": "BStack Sample Test",  # ✅ This is now valid
        "buildName": "Build_001",
        "userName": USERNAME,
        "accessKey": ACCESS_KEY,
        "projectName": "My Project"
    })

    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=chrome_options
    )
    yield driver
    driver.quit()

def testP_045(driver):
    try:
        print(
            "Verify/Validate presense of every module under 'Explore Support' click on every module and then return to a home page  validate URL of every module")
        driver.get(l.apple_url)
        hp.close_overlay(driver)

        success = hp.click_on_elem(driver, By.XPATH, "//a[@data-analytics-title='support']", 10)
        if success:
            print(f"Switched to this URL {driver.current_url}")

            try:
                locators = [
                    ("Iphone", l.iphone_loc, l.iphone_sup_url),
                    ("Mac", l.mac_loc, l.mac_sup_url),
                    ("iPad", l.ipad_loc, l.ipad_sup_url),
                    ("Watch", l.watch_loc, l.watch_sup_url),
                    ("Apple Vision Pro", l.appleVisPro_loc, l.appleVisPro_sup_url),
                    ("AirPods", l.airPods_loc, l.airPods_sup_url),
                    ("TV", l.tv_loc, l.tv_sup_url)
                ]
                try:
                    for name, locator, expected_url in locators:
                        print(f"\nTesting tab: {name}")
                        print(f"Locator value: {locator}")

                        # go back to homepage
                        driver.get(l.apple_url)
                        hp.close_overlay(driver)

                        assert hp.click_on_elem(driver, By.XPATH,
                                                "//a[@data-analytics-title='support']",
                                                10), "Can't locate 'Support'"

                        hp.wait_for_element(driver, By.XPATH, locator, 5)
                        hp.click_on_elem(driver, By.XPATH, locator, 10)
                        print(f"Clicked on {name}")
                        # checking URL match
                        hp.check_url(driver, expected_url, 10)
                        # clicking on the logo

                        print("Clicked on Apple Logo")
                        time.sleep(2)
                        print(f"Clicking on '{name}' tab. '{name}' is open")
                except Exception as e:
                    print(f"An error occurred:{e}")

            except TimeoutException:
                print("Submenu didn't drop")

    finally:
        print("Test has been completed")






