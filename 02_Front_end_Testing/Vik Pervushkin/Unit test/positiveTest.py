import time
import unittest

import HtmlTestRunner
import selenium
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
# chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeDriverManager

#fox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import AllureReports
import helpers as hp
import locators as l

#import HtmlTestRunner


class Positive_Chrome_TestApple(unittest.TestCase):

    def setUp(self):
        # Set up Chrome options
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--eager")

        #setting up driver

        self.driver = uc.Chrome(options=options)

    def tearDown(self):
        try:
            self.driver.quit()
        except Exception as e:
            print("Error during driver cleanup:", str(e))

    def test_036(self):
        print("Testing if video can be played")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver=self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator,10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.forgot_passw, 2,10)
        hp.click_on_elem(driver, By.XPATH, l.forgot_passw,10)
        print("Clicked on 'forgot password'")
        hp.scroll_down(driver, By.XPATH, l.play_button, 2 , 10)
        hp.click_and_check(driver, By.XPATH, l.play_button, l.vid_but,10)
        time.sleep(3)

    def test_037(self):
        print("Verify/Validate that search bar is working properly and finds 'Iphone repair'")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator,10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.sup_search)
        time.sleep(3)

        hp.enter_data(driver, By.XPATH, l.sup_search, "Iphone repair", 10)

        #lets's assert if the search matches
        try:
            elem = WebDriverWait(driver,10).until(
                EC.visibility_of_element_located((By.XPATH,"(//div[@class='SearchResult-url'])[1]"))
            )
            assert elem.is_displayed(), "Element is displayed"
            print(f"{elem.text} is displayed and matching the search")

        except Exception as e:
            print(F"search isn't validated:{e}")

    def test_038(self):
        print("Verify/Validate the 'form' gives an estimate price of a repair ")
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.repair_url)
        hp.scroll_down(driver, By.XPATH, l.service_dropdown)

        try:
            dropdown_xpaths = [
                l.service_dropdown,
                l.product_dropdown,
                l.model_dropdown,

            ]
            # using loop through each dropdown in sequence
            for index, xpath in enumerate(dropdown_xpaths, start=1):
                success = hp.select_from_dropdown(driver, xpath)
                if success:
                    print(f"Dropdown {index} selection successful.")
                else:
                    print(f"Failed to select from Dropdown {index}.")
        except Exception as e:
            print(f"error occurred :{e}")

        try:
            hp.click_on_elem(driver, By.XPATH, "(//button[@data-ss-analytics-event='acs.link_click'])[1]",10)
            time.sleep(3)
            print("clicked on a button")

            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//span[@class='stat-value'])[1]"))
            )
            print(f"the estimated price is :{elem.text}")
            driver.save_screenshot("price.png")

        except Exception as e:
            print(f"An error occurred: {e}")


    def test_039(self):
        print("Verify/Validate that link for YouTube works")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator ,10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.utube_link,5)
        hp.click_on_elem(driver, By.XPATH, l.utube_link,10)
        time.sleep(5)
        #checking URL
        current_url = driver.current_url
        self.assertEqual(l.utube_url, current_url, "YouTube wasn't opened ")
        print(f"Youtube was opened :{current_url}")

    def test_040(self):
        print("Verify/Validate functionality of a search bar on the main page")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver=self.driver
        driver.get(l.apple_url)
        time.sleep(5)
        hp.click_on_elem(driver,By.XPATH, l.searchBar,10)
        print("Clicked on search bar")
        time.sleep(3)
        hp.enter_data(driver,By.XPATH, l.searchBar1,"Iphone", 10)

        try:
            elem = WebDriverWait(driver,10).until(
                EC.visibility_of_element_located((By.XPATH,"(//a[contains(.,'iPhone')])[16]"))
            )
            assert elem.is_displayed(), "Element is not displayed"
            print(f"{elem.text} is displayed as search results")
        except Exception as e:
            print(F"search isn't validated:{e}")

    def test_041(self):
        print("Verify/Validate visibility of a unique text 'Apple support' in ")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver,By.XPATH, l.sup_locator,10)
        print("clicked on Support")
        time.sleep(3)
        hp.is_element_present(driver, By.XPATH, "//h1[contains(.,'Apple Support')]")

    def test_042(self):
        print("Verify/Validate visibility and functionality of Mac and Imac logos")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator,5)
        hp.click_on_elem(driver,By.XPATH, l.mac_sup_img,5)
        print(f"redirected into MAc Support:{driver.current_url}.Mac logo is visible and functional")
        hp.click_on_elem(driver, By.XPATH, l.imac_sup_img,5)
        print(f"Imac logo is visible and functional. The new page :{driver.current_url} was opened")


    def test_043(self):
        print("Verify/Validate that feedback can be left on feedback form in 'Learn about recovery mode")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver = self.driver
        driver.get(l.support_url)
        hp.scroll_down(driver,By.XPATH, l.forgot_passw, 10)
        hp.click_on_elem(driver, By.XPATH, l.forgot_passw,10)
        print("Clicked on 'Forgot Password'")
        hp.scroll_down(driver, By.XPATH, l.feedback_no,5)
        hp.click_on_elem(driver,By.XPATH,l.feedback_no,10)
        print("clicked on 'NO'")
        hp.random_text(driver, By.XPATH,l.text_area,50)
        hp.click_on_elem(driver, By.XPATH, l.submit_but,10)
        print("submitted feedback")
        driver.save_screenshot("")

    def test_044(self):
        print("Verify that submenu appears when 'Support' is hovered over")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver = self.driver
        driver.get(l.apple_url)
        #close any overlay/banner
        hp.close_overlay(driver)
        hp.click_on_elem(driver, By.XPATH, l.searchBar,10)

        result = hp.hover_and_wait_for_submenu(
            driver,
            hover_locator=(By.XPATH, "//a[@aria-label='Support']//span[@class='globalnav-link-text-container']"),
            submenu_locator=(By.XPATH, "//div[@id='globalnav-submenu-link-support']//div[@class='globalnav-flyout-content globalnav-submenu-content']")
        )

        if result:
            print("Submenu dropped successfully!")
        else:
            print("Submenu failed to drop.")

    def test_45(self):
        print("Verify/Validate presense of every module under 'Explore Support' click on every module and then return to a home page  validate URL of every module")
        try:
            self.driver.current_url
        except:
            self.setUp()
        driver = self.driver
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

                    #go back to homepage
                    driver.get(l.apple_url)
                    hp.close_overlay(driver)
                    self.assertTrue(
                        hp.click_on_elem(driver, By.XPATH,
                                              "//a[@data-analytics-title='support']",
                                              10),
                        "Can't locate 'Support'")

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

class Positive_Edge_TestApple(unittest.TestCase):
    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')  #ignores SSLs
        #options.add_argument("--headless")

        service = EdgeService(executable_path=r'C:\drivers\msedgedriver.exe')

        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.maximize_window()

    def tearDown(self):
        """safely quits to avoid (Error calling quit(): [WinError 6] The handle is invalid)"""
        try:
            #checking if driver is still responding
            self.driver.current_url
            print("Closing browser normally...")
            self.driver.quit()
        except (
                selenium.common.exceptions.WebDriverException,
                selenium.common.exceptions.NoSuchWindowException
        ):
            print("Browser was already closed. Skipping driver.quit().")
        finally:
            self.driver=None  #remove reference

    def test_036(self):
        print("Testing if video can be played")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.forgot_passw, 2, 10)
        hp.click_on_elem(driver, By.XPATH, l.forgot_passw, 10)
        print("Clicked on 'forgot password'")
        hp.scroll_down(driver, By.XPATH, l.play_button, 2, 10)
        hp.click_and_check(driver, By.XPATH, l.play_button, l.vid_but, 10)
        time.sleep(3)

    def test_037(self):
        print("Verify/Validate that search bar is working properly and finds 'Iphone repair'")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.sup_search)
        time.sleep(3)

        hp.enter_data(driver, By.XPATH, l.sup_search, "Iphone repair", 10)

        # lets's assert if the search matches
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//div[@class='SearchResult-url'])[1]"))
            )
            assert elem.is_displayed(), "Element is displayed"
            print(f"{elem.text} is displayed and matching the search")

        except Exception as e:
            print(F"search isn't validated:{e}")

    def test_038(self):
        print("Verify/Validate the 'form' gives an estimate price of a repair ")
        driver = self.driver
        driver.get(l.repair_url)
        hp.scroll_down(driver, By.XPATH, l.service_dropdown)

        try:
            dropdown_xpaths = [
                l.service_dropdown,
                l.product_dropdown,
                l.model_dropdown,

            ]
            # using loop through each dropdown in sequence
            for index, xpath in enumerate(dropdown_xpaths, start=1):
                success = hp.select_from_dropdown(driver, xpath)
                if success:
                    print(f"Dropdown {index} selection successful.")
                else:
                    print(f"Failed to select from Dropdown {index}.")
        except Exception as e:
            print(f"error occurred :{e}")

        try:
            hp.click_on_elem(driver, By.XPATH, "(//button[@data-ss-analytics-event='acs.link_click'])[1]", 10)
            time.sleep(3)
            print("clicked on a button")

            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//span[@class='stat-value'])[1]"))
            )
            print(f"the estimated price is :{elem.text}")
            driver.save_screenshot("price.png")

        except Exception as e:
            print(f"An error occurred: {e}")

    def test_039(self):
        print("Verify/Validate that link for YouTube works")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.utube_link, 5)
        hp.click_on_elem(driver, By.XPATH, l.utube_link, 10)
        time.sleep(5)
        # checking URL
        current_url = driver.current_url
        self.assertEqual(l.utube_url, current_url, "YouTube wasn't opened ")
        print(f"Youtube was opened :{current_url}")

    def test_040(self):
        print("Verify/Validate functionality of a search bar on the main page")
        driver = self.driver
        driver.get(l.apple_url)
        time.sleep(5)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        print("Clicked on search bar")
        time.sleep(3)
        hp.enter_data(driver, By.XPATH, l.searchBar1, "Iphone", 10)

        try:
            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'iPhone')])[16]"))
            )
            assert elem.is_displayed(), "Element is not displayed"
            print(f"{elem.text} is displayed as search results")
        except Exception as e:
            print(F"search isn't validated:{e}")

    def test_041(self):
        print("Verify/Validate visibility of a unique text 'Apple support' in ")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on Support")
        time.sleep(3)
        hp.is_element_present(driver, By.XPATH, "//h1[contains(.,'Apple Support')]")

    def test_042(self):
        print("Verify/Validate visibility and functionality of Mac and Imac logos")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 5)
        hp.click_on_elem(driver, By.XPATH, l.mac_sup_img, 5)
        print(f"redirected into MAc Support:{driver.current_url}.Mac logo is visible and functional")
        hp.click_on_elem(driver, By.XPATH, l.imac_sup_img, 5)
        print(f"Imac logo is visible and functional. The new page :{driver.current_url} was opened")

    def test_043(self):
        print("Verify/Validate that feedback can be left on feedback form in 'Learn about recovery mode")
        driver = self.driver
        driver.get(l.support_url)
        hp.scroll_down(driver, By.XPATH, l.forgot_passw, 10)
        hp.click_on_elem(driver, By.XPATH, l.forgot_passw, 10)
        print("Clicked on 'Forgot Password'")
        hp.scroll_down(driver, By.XPATH, l.feedback_no, 5)
        hp.click_on_elem(driver, By.XPATH, l.feedback_no, 10)
        print("clicked on 'NO'")
        hp.random_text(driver, By.XPATH, l.text_area, 50)
        hp.click_on_elem(driver, By.XPATH, l.submit_but, 10)
        print("submitted feedback")
        driver.save_screenshot("")

    def test_044(self):
        print("Verify that submenu appears when 'Support' is hovered over")
        driver = self.driver
        driver.get(l.apple_url)
        # close any overlay/banner
        hp.close_overlay(driver)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)

        result = hp.hover_and_wait_for_submenu(
            driver,
            hover_locator=(By.XPATH, "//a[@aria-label='Support']//span[@class='globalnav-link-text-container']"),
            submenu_locator=(By.XPATH,
                             "//div[@id='globalnav-submenu-link-support']//div[@class='globalnav-flyout-content globalnav-submenu-content']")
        )

        if result:
            print("Submenu dropped successfully!")
        else:
            print("Submenu failed to drop.")

    def test_45(self):
        driver = self.driver
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
                    self.assertTrue(
                        hp.click_on_elem(driver, By.XPATH,
                                         "//a[@data-analytics-title='support']",
                                         10),
                        "Can't locate 'Support'")

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

class Positive_FireFox_TestApple(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        # Set up Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # headless mode

        # Optional: Add other useful arguments
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--ignore-certificate-errors')
        options.page_load_strategy = 'eager'
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                                        options=options)
        self.driver.maximize_window()

    def tearDown(self):
        """safely quits to avoid (Error calling quit(): [WinError 6] The handle is invalid)"""
        try:
            # checking if driver is still responding
            self.driver.current_url
            print("Closing browser normally...")
            self.driver.quit()
        except (
                selenium.common.exceptions.WebDriverException,
                selenium.common.exceptions.NoSuchWindowException
        ):
            print("Browser was already closed. Skipping driver.quit().")
        finally:
            self.driver = None  # remove reference




    def test_036(self):
        print("Testing if video can be played")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.forgot_passw, 2, 10)
        hp.click_on_elem(driver, By.XPATH, l.forgot_passw, 10)
        print("Clicked on 'forgot password'")
        hp.scroll_down(driver, By.XPATH, l.play_button, 2, 10)
        hp.click_and_check(driver, By.XPATH, l.play_button, l.vid_but, 10)
        time.sleep(3)

    def test_037(self):
        print("Verify/Validate that search bar is working properly and finds 'Iphone repair'")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.sup_search)
        time.sleep(3)

        hp.enter_data(driver, By.XPATH, l.sup_search, "Iphone repair", 10)

        # lets's assert if the search matches
        try:
            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//div[@class='SearchResult-url'])[1]"))
            )
            assert elem.is_displayed(), "Element is displayed"
            print(f"{elem.text} is displayed and matching the search")

        except Exception as e:
            print(F"search isn't validated:{e}")

    def test_038(self):
        print("Verify/Validate the 'form' gives an estimate price of a repair ")
        driver = self.driver
        driver.get(l.repair_url)
        hp.scroll_down(driver, By.XPATH, l.service_dropdown)

        try:
            dropdown_xpaths = [
                l.service_dropdown,
                l.product_dropdown,
                l.model_dropdown,

            ]
            # using loop through each dropdown in sequence
            for index, xpath in enumerate(dropdown_xpaths, start=1):
                success = hp.select_from_dropdown(driver, xpath)
                if success:
                    print(f"Dropdown {index} selection successful.")
                else:
                    print(f"Failed to select from Dropdown {index}.")
        except Exception as e:
            print(f"error occurred :{e}")

        try:
            hp.click_on_elem(driver, By.XPATH, "(//button[@data-ss-analytics-event='acs.link_click'])[1]", 10)
            time.sleep(3)
            print("clicked on a button")

            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//span[@class='stat-value'])[1]"))
            )
            print(f"the estimated price is :{elem.text}")
            driver.save_screenshot("price.png")

        except Exception as e:
            print(f"An error occurred: {e}")

    def test_039(self):
        print("Verify/Validate that link for YouTube works")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on 'Support'")
        hp.scroll_down(driver, By.XPATH, l.utube_link, 5)
        hp.click_on_elem(driver, By.XPATH, l.utube_link, 10)
        time.sleep(5)
        # checking URL
        current_url = driver.current_url
        self.assertEqual(l.utube_url, current_url, "YouTube wasn't opened ")
        print(f"Youtube was opened :{current_url}")

    def test_040(self):
        print("Verify/Validate functionality of a search bar on the main page")
        driver = self.driver
        driver.get(l.apple_url)
        time.sleep(5)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        print("Clicked on search bar")
        time.sleep(3)
        hp.enter_data(driver, By.XPATH, l.searchBar1, "Iphone", 10)

        try:
            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'iPhone')])[16]"))
            )
            assert elem.is_displayed(), "Element is not displayed"
            print(f"{elem.text} is displayed as search results")
        except Exception as e:
            print(F"search isn't validated:{e}")

    def test_041(self):
        print("Verify/Validate visibility of a unique text 'Apple support' in ")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 10)
        print("clicked on Support")
        time.sleep(3)
        hp.is_element_present(driver, By.XPATH, "//h1[contains(.,'Apple Support')]")

    def test_042(self):
        print("Verify/Validate visibility and functionality of Mac and Imac logos")
        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.sup_locator, 5)
        hp.click_on_elem(driver, By.XPATH, l.mac_sup_img, 5)
        print(f"redirected into MAc Support:{driver.current_url}.Mac logo is visible and functional")
        hp.click_on_elem(driver, By.XPATH, l.imac_sup_img, 5)
        print(f"Imac logo is visible and functional. The new page :{driver.current_url} was opened")

    def test_043(self):
        print("Verify/Validate that feedback can be left on feedback form in 'Learn about recovery mode")
        driver = self.driver
        driver.get(l.support_url)
        hp.scroll_down(driver, By.XPATH, l.forgot_passw, 10)
        hp.click_on_elem(driver, By.XPATH, l.forgot_passw, 10)
        print("Clicked on 'Forgot Password'")
        hp.scroll_down(driver, By.XPATH, l.feedback_no, 5)
        hp.click_on_elem(driver, By.XPATH, l.feedback_no, 10)
        print("clicked on 'NO'")
        hp.random_text(driver, By.XPATH, l.text_area, 50)
        hp.click_on_elem(driver, By.XPATH, l.submit_but, 10)
        print("submitted feedback")
        driver.save_screenshot("")

    def test_044(self):
        print("Verify that submenu appears when 'Support' is hovered over")
        driver = self.driver
        driver.get(l.apple_url)
        # close any overlay/banner
        hp.close_overlay(driver)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)

        result = hp.hover_and_wait_for_submenu(
            driver,
            hover_locator=(By.XPATH, "//a[@aria-label='Support']//span[@class='globalnav-link-text-container']"),
            submenu_locator=(By.XPATH,
                             "//div[@id='globalnav-submenu-link-support']//div[@class='globalnav-flyout-content globalnav-submenu-content']")
        )

        if result:
            print("Submenu dropped successfully!")
        else:
            print("Submenu failed to drop.")

    def test_045(self):
        driver = self.driver
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
                    self.assertTrue(
                        hp.click_on_elem(driver, By.XPATH,
                                         "//a[@data-analytics-title='support']",
                                         10),
                        "Can't locate 'Support'")

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


if __name__ == '__main__':
    unittest.main(AllureReports)















    
























