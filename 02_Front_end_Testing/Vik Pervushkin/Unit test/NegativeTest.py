import time
import unittest

import selenium
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
#chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# edge
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options
#
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# firefox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
# import HtmlTestRunner
import AllureReports
import helpers as hp
import locators as l



class Chrome_NegativeTestApple(unittest.TestCase):
    def setUp(self):
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        #options.add_argument("--eager")

        # setting up driver

        self.driver = webdriver.Chrome(options=options)

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



    def test_N_036(self):
        print("Enter special characters only (e.g., !@#$%^&*) in the search box")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar,10)
        hp.enter_data(driver, By.XPATH, l.searchBar1,"!@#$%^&*",10)
        try:
            error_message = WebDriverWait(driver, 10). until(
                EC.visibility_of_element_located((By.XPATH,"//h2[contains(.,'HTTP ERROR 400 Ambiguous URI path encoding')]"))
            )
            self.assertIn("HTTP ERROR 400 Ambiguous URI path encoding", error_message.text,
                          f"Expected error message not found. Got:'{error_message.text}'")
            print(error_message.text)
            print("Error message displayed correctly")
        except NoSuchElementException:
            print("No such element found")

    def test_N_037(self):
        print("Use non-supported languages or symbols (e.g., Chinese/Japanese characters if not supported).")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        hp.enter_data(driver, By.XPATH, l.searchBar1, "你好,不客氣", 10)
        hp.delay()
        if driver.current_url != l.apple_url:
            print(f"{driver.current_url} new tab was open")
            try:
                error_message = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='rf-serp-nullsearch-title' and contains(text(), 'Sorry, no matches were found.')]"))
                )
                self.assertIn("Sorry, no matches were found.", error_message.text,
                              f"Expected error message not found. Got: '{error_message.text}'")
                print(error_message.text)
            except NoSuchElementException:
                print("No such element found")


    def test_N_038(self):
        print("Enter a long string into a search bar")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        try:
            elem = WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH, l.searchBar1))
            )
            elem.click()
            long_string = hp.generate_long_string(10000)
            print("generated long string was accepted into a search bar ")
            print(long_string[:100])
            elem.send_keys(long_string)
            elem.send_keys(Keys.ENTER)
        except Exception:
            return False

    def test_N_039(self):
        print("Try to navigate back/forward rapidly using browser buttons.")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        time.sleep(3)
        hp.back_and_forward(driver,l.apple_url, By.XPATH, l.sup_locator)


    def test_N_040(self):
        print("Empty Search Submission")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        hp.delay()
        hp.enter_data(driver, By.XPATH, l.searchBar1,"",10)
        try:
            if driver.current_url ==l.apple_url:
                print("An empty string is not accepted and search wasn't initiated ")
        except Exception as e:
            self.fail(f"An error occurred while accessing search bar: {str(e)}")

    def test_N_041(self):
        print("Using fake credentials to log in")
        #restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_sign_in_ur)
        hp.delay()
        hp.switchTo_IframeBy_id(driver, "aid-auth-widget-iFrame",10 )
        #enteriing email into the username table
        hp.fake_logIn(driver, email_by=By.ID,
                      email_value= 'account_name_text_field',
                      password_by= By.ID,
                      password_value= 'password_text_field',
                      timeout=10
                      )
        hp.delay()
        if driver.current_url == "https://account.apple.com/sign-in":
            print(f" Page's URL :{driver.current_url} A fake user can't log in")
        else:
            print("test failed")



    def test_N_042(self):
        print("Validate that 'Apple support video' on YouTube isn't found with JS disabled ")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        #Chrome options to disable JavaScript
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-javascript")
        chrome_options.add_argument("--disable-features=JavaScript")


        chrome_prefs = {
            "profile.default_content_setting_values.javascript": 2,
            "profile.managed_default_content_settings.javascript": 2
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)
        chrome_options.add_argument("--disable-application-cache")
        chrome_options.add_argument("--disable-cache")

        driver = webdriver.Chrome(options=chrome_options)
        self.driver = driver  # Make sure tearDown can close it
        driver.maximize_window()

        try:
            #confirm JS is truly OFF
            driver.get("data:text/html;charset=utf-8,<script>document.write('JS is ON')</script>")
            body_text = driver.find_element(By.TAG_NAME, "body").text
            assert body_text == "", "JavaScript should be OFF"
            print("JavaScript is successfully disabled")

            #navigate to Apple website
            driver.get(l.apple_url)

            #click o Support section
            hp.click_on_elem(driver, By.XPATH, l.sup_locator, timeout=10)

            #scroll down  YouTube section
            hp.scroll_down(driver, By.XPATH, l.apple_sup_on_utube, timeout=5)

            #click on "Visit Apple Support on YouTube"
            hp.click_on_elem(driver, By.XPATH, "//span[contains(.,'Visit Apple Support on YouTube')]", timeout=10)

            #wait until correct URL loads
            WebDriverWait(driver, 10).until(
                lambda d: "youtube.com/applesupport" in d.current_url
            )
            print("Navigated to:", driver.current_url)

            #wait for video element (may not exist without JS)
            try:
                video_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//video[contains(@class, 'html5-main-video')]"))
                )
                print("Video element found")

                # Try to play (will likely also fail)
                try:
                    driver.execute_script("arguments[0].play();", video_element)
                    print("Video started playing")
                except Exception as e:
                    print(f" Could not play video: {e}")
                    driver.save_screenshot("video_play_failed.png")

            except TimeoutException:
                print("Video element not found — expected behavior when JavaScript is OFF")
                driver.save_screenshot("js_off_video_not_loaded.png")
        except Exception as e:
            print(f"An error occurred:{e}")

    def test_N_043(self):
        print("Validate if an email field accepts emails without a domain and @")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver = self.driver
        driver.get("https://account.apple.com/sign-in")
        hp.delay()
        hp.switchTo_IframeBy_id(driver, "aid-auth-widget-iFrame", 10)
        #enteriing email into the username table
        self.assertTrue(
        hp.enter_data(driver, By.ID, "account_name_text_field", "viktor.com",10),"Wrong Email format wasn't entered")


    def test_N_044(self):
        print("Enter paces only into a search bar of a main page ")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver=self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar,10)
        print("attempting to enter 100 spaces")
        hp.space_input(driver, By.XPATH, l.searchBar1,100)


    def test_N_045(self):
        print("Enter non existent zip code in order to locate nearest Apple store")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver= self.driver
        driver.get(l.apple_url)

        try:
            # Scroll to and click Find Store
            hp.scroll_down(driver, By.XPATH, l.find_store, 3)
            hp.click_on_elem(driver, By.XPATH, l.find_store, 3)
            print("Entering zip code")
            #locate and enter zip code into field
            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            elem.click()
            elem.send_keys("123456789123456789")
            time.sleep(2)
            elem.send_keys(Keys.ENTER)
            #debug flow
            print("Current URL:", driver.current_url)
            print("Page title:", driver.title)
            #driver.save_screenshot("after_typing_zip.png")
            time.sleep(3)
            print("Entered non-existent zip code '123456789'")
            #delay to let error message appear
            time.sleep(5)
            # Wait for error message to appear
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'No results found for “123456789”')]"))
            )
            # Assert expected message text
            self.assertIn("No results found for", error_message.text.lower(),
                          "Error message did not contain expected text")
            print("Error message shown:", error_message.text)

        except Exception as e:
            print(f"Test failed: {str(e)}")
            driver.save_screenshot("test_failure.png")

class Edge_NegativeTestApple(unittest.TestCase):
    def setUp(self):
        options = EdgeOptions()
        options.add_argument('--ignore-certificate-errors')  # ignores SSLs
        # options.add_argument("--headless")

        service = EdgeService(executable_path=r'C:\drivers\msedgedriver.exe')

        self.driver = webdriver.Edge(service=service, options=options)
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

    def test_N_036(self):
        print("Enter special characters only (e.g., !@#$%^&*) in the search box")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar,10)
        hp.enter_data(driver, By.XPATH, l.searchBar1,"!@#$%^&*",10)
        try:
            error_message = WebDriverWait(driver, 10). until(
                EC.visibility_of_element_located((By.XPATH,"//h2[contains(.,'HTTP ERROR 400 Ambiguous URI path encoding')]"))
            )
            self.assertIn("HTTP ERROR 400 Ambiguous URI path encoding", error_message.text,
                          f"Expected error message not found. Got:'{error_message.text}'")
            print(error_message.text)
            print("Error message displayed correctly")
        except NoSuchElementException:
            print("No such element found")

    def test_N_037(self):
        print("Use non-supported languages or symbols (e.g., Chinese/Japanese characters if not supported).")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        hp.enter_data(driver, By.XPATH, l.searchBar1, "你好,不客氣", 10)
        hp.delay()
        if driver.current_url != l.apple_url:
            print(f"{driver.current_url} new tab was open")
            try:
                error_message = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='rf-serp-nullsearch-title' and contains(text(), 'Sorry, no matches were found.')]"))
                )
                self.assertIn("Sorry, no matches were found.", error_message.text,
                              f"Expected error message not found. Got: '{error_message.text}'")
                print(error_message.text)
            except NoSuchElementException:
                print("No such element found")


    def test_N_038(self):
        print("Enter a long string into a search bar")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        try:
            elem = WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH, l.searchBar1))
            )
            elem.click()
            long_string = hp.generate_long_string(10000)
            print("generated long string was accepted into a search bar ")
            print(long_string[:100])
            elem.send_keys(long_string)
            elem.send_keys(Keys.ENTER)
        except Exception:
            return False

    def test_N_039(self):
        print("Try to navigate back/forward rapidly using browser buttons.")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        time.sleep(3)
        hp.back_and_forward(driver,l.apple_url, By.XPATH, l.sup_locator)


    def test_N_040(self):
        print("Empty Search Submission")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        hp.delay()
        hp.enter_data(driver, By.XPATH, l.searchBar1,"",10)
        try:
            if driver.current_url ==l.apple_url:
                print("An empty string is not accepted and search wasn't initiated ")
        except Exception as e:
            self.fail(f"An error occurred while accessing search bar: {str(e)}")

    def test_N_041(self):
        print("Using fake credentials to log in")
        #restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_sign_in_ur)
        hp.delay()
        hp.switchTo_IframeBy_id(driver, "aid-auth-widget-iFrame",10 )
        #enteriing email into the username table
        hp.fake_logIn(driver, email_by=By.ID,
                      email_value= 'account_name_text_field',
                      password_by= By.ID,
                      password_value= 'password_text_field',
                      timeout=10
                      )
        hp.delay()
        if driver.current_url == "https://account.apple.com/sign-in":
            print(f" Page's URL :{driver.current_url} A fake user can't log in")
        else:
            print("test failed")



    def test_N_042(self):
        print("Validate that 'Apple support video' on YouTube isn't found with JS disabled")

        edge_options = EdgeOptions()
        prefs = {
            "profile.managed_default_content_settings.javascript": 2,
            "profile.default_content_setting_values.javascript": 2
        }

        edge_options.add_experimental_option("prefs", prefs)

        # Optional: Disable cache to ensure clean test
        edge_options.add_argument("--disable-application-cache")
        edge_options.add_argument("--disable-cache")

        # Use webdriver-manager to handle driver

        driver = self.driver
        driver.maximize_window()


    def test_N_043(self):
        print("Validate if an email field accepts emails without a domain and @")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver = self.driver
        driver.get("https://account.apple.com/sign-in")
        hp.delay()
        hp.switchTo_IframeBy_id(driver, "aid-auth-widget-iFrame", 10)
        #enteriing email into the username table
        self.assertTrue(
        hp.enter_data(driver, By.ID, "account_name_text_field", "viktor.com",10),"Wrong Email format wasn't entered")


    def test_N_044(self):
        print("Enter paces only into a search bar of a main page ")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver=self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar,10)
        print("attempting to enter 100 spaces")
        hp.space_input(driver, By.XPATH, l.searchBar1,100)


    def test_N_045(self):
        print("Enter non existent zip code in order to locate nearest Apple store")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver= self.driver
        driver.get(l.apple_url)

        try:
            # Scroll to and click Find Store
            hp.scroll_down(driver, By.XPATH, l.find_store, 3)
            hp.click_on_elem(driver, By.XPATH, l.find_store, 3)
            print("Entering zip code")
            #locate and enter zip code into field
            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            elem.click()
            elem.send_keys("123456789123456789")
            time.sleep(2)
            elem.send_keys(Keys.ENTER)
            #debug flow
            print("Current URL:", driver.current_url)
            print("Page title:", driver.title)
            #driver.save_screenshot("after_typing_zip.png")
            time.sleep(3)
            print("Entered non-existent zip code '123456789'")
            #delay to let error message appear
            time.sleep(5)
            # Wait for error message to appear
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'No results found for “123456789”')]"))
            )
            # Assert expected message text
            self.assertIn("No results found for", error_message.text.lower(),
                          "Error message did not contain expected text")
            print("Error message shown:", error_message.text)

        except Exception as e:
            print(f"Test failed: {str(e)}")
            driver.save_screenshot("test_failure.png")

class FireFox_Negative_Test(unittest.TestCase):
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
        #options.add_argument("--headless")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                                        options=options)
        self.driver.maximize_window()

    def tearDown(self):
        print("Closing browser...")
        self.driver.quit()
        print("Browser closed.")


    def test_N_036(self):
        print("Enter special characters only (e.g., !@#$%^&*) in the search box")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar,10)
        hp.enter_data(driver, By.XPATH, l.searchBar1,"!@#$%^&*",10)
        try:
            error_message = WebDriverWait(driver, 10). until(
                EC.visibility_of_element_located((By.XPATH,"//h2[contains(.,'HTTP ERROR 400 Ambiguous URI path encoding')]"))
            )
            self.assertIn("HTTP ERROR 400 Ambiguous URI path encoding", error_message.text,
                          f"Expected error message not found. Got:'{error_message.text}'")
            print(error_message.text)
            print("Error message displayed correctly")
        except NoSuchElementException:
            print("No such element found")

    def test_N_037(self):
        print("Use non-supported languages or symbols (e.g., Chinese/Japanese characters if not supported).")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        hp.enter_data(driver, By.XPATH, l.searchBar1, "你好,不客氣", 10)
        hp.delay()
        if driver.current_url != l.apple_url:
            print(f"{driver.current_url} new tab was open")
            try:
                error_message = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='rf-serp-nullsearch-title' and contains(text(), 'Sorry, no matches were found.')]"))
                )
                self.assertIn("Sorry, no matches were found.", error_message.text,
                              f"Expected error message not found. Got: '{error_message.text}'")
                print(error_message.text)
            except NoSuchElementException:
                print("No such element found")


    def test_N_038(self):
        print("Enter a long string into a search bar")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        try:
            elem = WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH, l.searchBar1))
            )
            elem.click()
            long_string = hp.generate_long_string(10000)
            print("generated long string was accepted into a search bar ")
            print(long_string[:100])
            elem.send_keys(long_string)
            elem.send_keys(Keys.ENTER)
        except Exception:
            return False

    def test_N_039(self):
        print("Try to navigate back/forward rapidly using browser buttons.")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        time.sleep(3)
        hp.back_and_forward(driver,l.apple_url, By.XPATH, l.sup_locator)


    def test_N_040(self):
        print("Empty Search Submission")
        # restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar, 10)
        hp.delay()
        hp.enter_data(driver, By.XPATH, l.searchBar1,"",10)
        try:
            if driver.current_url ==l.apple_url:
                print("An empty string is not accepted and search wasn't initiated ")
        except Exception as e:
            self.fail(f"An error occurred while accessing search bar: {str(e)}")

    def test_N_041(self):
        print("Using fake credentials to log in")
        #restart browser if needed
        try:
            self.driver.current_url
        except:
            self.setUp()

        driver = self.driver
        driver.get(l.apple_sign_in_ur)
        hp.delay()
        hp.switchTo_IframeBy_id(driver, "aid-auth-widget-iFrame",10 )
        #enteriing email into the username table
        hp.fake_logIn(driver, email_by=By.ID,
                      email_value= 'account_name_text_field',
                      password_by= By.ID,
                      password_value= 'password_text_field',
                      timeout=10
                      )
        hp.delay()
        if driver.current_url == "https://account.apple.com/sign-in":
            print(f" Page's URL :{driver.current_url} A fake user can't log in")
        else:
            print("test failed")



    def test_N_042(self):
        print("Validate that 'Apple support video' on YouTube isn't found with JS disabled ")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        # disable JS on FireFox
        firefox_options = Options()
        firefox_options.set_preference("browser.cache.disk.enable", False)
        firefox_options.set_preference("browser.cache.memory.enable", False)
        firefox_options.set_preference("browser.cache.offline.enable", False)
        firefox_options.set_preference("network.http.referer.default_policy", 2)

        driver = webdriver.Firefox(options=firefox_options)

        self.driver = driver  # Assign to self so tearDown can close it
        driver.maximize_window()

        try:
            #confirm JS is truly OFF
            driver.get("data:text/html;charset=utf-8,<script>document.write('JS is ON')</script>")
            body_text = driver.find_element(By.TAG_NAME, "body").text
            assert body_text == "", "JavaScript should be OFF"
            print("JavaScript is successfully disabled")

            #navigate to Apple website
            driver.get(l.apple_url)

            #click on Support section
            hp.click_on_elem(driver, By.XPATH, l.sup_locator, timeout=10)

            #scroll down  YouTube section
            hp.scroll_down(driver, By.XPATH, l.apple_sup_on_utube, timeout=5)

            #click on "Visit Apple Support on YouTube"
            hp.click_on_elem(driver, By.XPATH, "//span[contains(.,'Visit Apple Support on YouTube')]", timeout=10)

            #wait until correct URL loads
            WebDriverWait(driver, 10).until(
                lambda d: "youtube.com/applesupport" in d.current_url
            )
            print("Navigated to:", driver.current_url)

            #wait for video element (may not exist without JS)
            try:
                video_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//video[contains(@class, 'html5-main-video')]"))
                )
                print("Video element found")

                # Try to play (will likely also fail)
                try:
                    driver.execute_script("arguments[0].play();", video_element)
                    print("Video started playing")
                except Exception as e:
                    print(f" Could not play video: {e}")
                    driver.save_screenshot("video_play_failed.png")

            except TimeoutException:
                print("Video element not found — expected behavior when JavaScript is OFF")
                driver.save_screenshot("js_off_video_not_loaded.png")
        except Exception as e:
            print(f"An error occurred:{e}")

    def test_N_043(self):
        print("Validate if an email field accepts emails without a domain and @")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver = self.driver
        driver.get("https://account.apple.com/sign-in")
        hp.delay()
        hp.switchTo_IframeBy_id(driver, "aid-auth-widget-iFrame", 10)
        #enteriing email into the username table
        self.assertTrue(
        hp.enter_data(driver, By.ID, "account_name_text_field", "viktor.com",10),"Wrong Email format wasn't entered")


    def test_N_044(self):
        print("Enter paces only into a search bar of a main page ")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver=self.driver
        driver.get(l.apple_url)
        hp.click_on_elem(driver, By.XPATH, l.searchBar,10)
        print("attempting to enter 100 spaces")
        hp.space_input(driver, By.XPATH, l.searchBar1,100)


    def test_N_045(self):
        print("Enter non existent zip code in order to locate nearest Apple store")
        try:
            self.driver.current_url
        except:
            print("Browser was closed. Restarting...")
            self.setUp()

        driver= self.driver
        driver.get(l.apple_url)

        try:
            # Scroll to and click Find Store
            hp.scroll_down(driver, By.XPATH, l.find_store, 3)
            hp.click_on_elem(driver, By.XPATH, l.find_store, 3)
            print("Entering zip code")
            #locate and enter zip code into field
            elem = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
            )
            elem.click()
            elem.send_keys("123456789123456789")
            time.sleep(2)
            elem.send_keys(Keys.ENTER)
            #debug flow
            print("Current URL:", driver.current_url)
            print("Page title:", driver.title)
            #driver.save_screenshot("after_typing_zip.png")
            time.sleep(3)
            print("Entered non-existent zip code '123456789'")
            #delay to let error message appear
            time.sleep(5)
            # Wait for error message to appear
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'No results found for “123456789”')]"))
            )
            # Assert expected message text
            self.assertIn("No results found for", error_message.text.lower(),
                          "Error message did not contain expected text")
            print("Error message shown:", error_message.text)

        except Exception as e:
            print(f"Test failed: {str(e)}")
            driver.save_screenshot("test_failure.png")

if __name__ == '__main__':
    unittest.main(AllureReports)




































