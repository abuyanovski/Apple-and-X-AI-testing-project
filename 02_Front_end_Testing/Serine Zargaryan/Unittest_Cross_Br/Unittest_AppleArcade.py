#import AllureReports
#import HtmlTestRunner
import random
import time
import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def delay():
    time.sleep(random.randint(1, 5))


class ChromePositiveTestCases(unittest.TestCase):
    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_case_016_positive_apple_arcade(self):
        # Verify "Try it free" button works
        driver = self.driver
        print("Test Case 016 - try free button")

        driver.get("https://www.apple.com/apple-arcade/")

        try_it_free = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Try it free')]"))
        )
        try_it_free.click()
        time.sleep(2)

        current_url = driver.current_url.lower()
        self.assertTrue("apple.com" in current_url or "apps.apple.com" in current_url)

    def test_case_017_positive_apple_arcade(self):
        # Verify external App Store links work
        driver = self.driver
        print("Test Case 017 - external App Store links")

        driver.get("https://www.apple.com/apple-arcade/")

        # Wait for the first App Store link to be present
        game_card = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'apps.apple.com')]"))
        )
        # Scroll to the App Store link smoothly and center it in the viewport
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", game_card)
        time.sleep(2)

        # Click the App Store link
        game_card.click()
        time.sleep(2)

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])

        # Verify that the current URL contains 'apps.apple.com'
        current_url = driver.current_url.lower()
        self.assertIn("apps.apple.com", current_url)

    def test_case_018_positive_apple_arcade(self):
        # Verify FAQ item expands on click
        driver = self.driver
        print("Test Case 018 - FAQ expand on click")

        driver.get("https://www.apple.com/apple-arcade/")

        # Scroll to the FAQ section header
        faq_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)
        time.sleep(2)

        faq_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-controls, 'accordion')]"))
        )
        faq_button.click()
        time.sleep(4)

        expanded = faq_button.get_attribute("aria-expanded")
        self.assertEqual(expanded, "true")

    def test_case_019_positive_apple_arcade(self):
        driver = self.driver
        print("Test Case 019 - FAQ accessibility with keyboard")

        driver.get("https://www.apple.com/apple-arcade/")

        # Locate the FAQ section header by XPath
        faq_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )

        # Scroll to the FAQ header to bring FAQ into view
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)
        time.sleep(1)

        # Focus on the body element
        body = driver.find_element(By.TAG_NAME, "body")

        # Press TAB once - focus should move to the first FAQ toggle button
        body.send_keys(Keys.TAB)
        time.sleep(2)

        # Get the currently focused element (expected first FAQ button)
        focused = driver.switch_to.active_element

        # Store unique attribute to refind the element later
        aria_controls = focused.get_attribute("aria-controls")

        # Press ENTER to expand the FAQ item
        focused.send_keys(Keys.ENTER)
        time.sleep(2)

        # Re-find the FAQ button after DOM update
        refreshed_faq_button = driver.find_element(By.XPATH, f"//button[@aria-controls='{aria_controls}']")

        # Verify that the FAQ item expanded (aria-expanded="true")
        expanded = refreshed_faq_button.get_attribute("aria-expanded")
        self.assertEqual(expanded, "true", "FAQ item did not expand after ENTER key")

    def test_case_020_positive_apple_arcade(self):
        # Verify video banner playback
        driver = self.driver
        print("Test Case 020 - Verify video banner playback")

        driver.get("https://www.apple.com/apple-arcade/")

        wait = WebDriverWait(driver, 15)

        # Wait for the video element
        video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))

        # Try to find and click the pause button
        try:
            pause_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='pause hero video']")
            ))
            pause_button.click()
            time.sleep(2)

            # Check that video is paused
            is_paused = driver.execute_script("return arguments[0].paused;", video)
            self.assertTrue(is_paused, "Video did not pause after clicking Pause button")
        except TimeoutException:
            # If pause button not found, check if video is already paused
            is_paused = driver.execute_script("return arguments[0].paused;", video)
            if not is_paused:
                self.fail("Pause button not found and video is playing")

        # Find the play button and click it
        play_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='play hero video']")
        ))
        play_button.click()
        time.sleep(3)

        # Verify that video is playing
        is_playing = driver.execute_script("return !arguments[0].paused;", video)
        self.assertTrue(is_playing, "Video did not start playing after clicking Play button")

    def tearDown(self):
        self.driver.quit()

class FirefoxPositiveTests(unittest.TestCase):
    def setUp(self):
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Firefox(service=service, options=options)

    def test_case_016_positive_apple_arcade(self):
        # Verify "Try it free" button works
        driver = self.driver
        print("Test Case 016 - try free button")

        driver.get("https://www.apple.com/apple-arcade/")

        try_it_free = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Try it free')]"))
        )
        try_it_free.click()
        time.sleep(2)

        current_url = driver.current_url.lower()
        self.assertTrue("apple.com" in current_url or "apps.apple.com" in current_url)

    def test_case_017_positive_apple_arcade(self):
        # Verify external App Store links work
        driver = self.driver
        print("Test Case 017 - external App Store links")

        driver.get("https://www.apple.com/apple-arcade/")

        # Wait for the first App Store link to be present
        game_card = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'apps.apple.com')]"))
        )
        # Scroll to the App Store link smoothly and center it in the viewport
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", game_card)
        time.sleep(2)

        # Click the App Store link
        game_card.click()
        time.sleep(2)

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])

        # Verify that the current URL contains 'apps.apple.com'
        current_url = driver.current_url.lower()
        self.assertIn("apps.apple.com", current_url)

    def test_case_018_positive_apple_arcade(self):
        # Verify FAQ item expands on click
        driver = self.driver
        print("Test Case 018 - FAQ expand on click")

        driver.get("https://www.apple.com/apple-arcade/")

        # Scroll to the FAQ section header
        faq_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)
        time.sleep(2)

        faq_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-controls, 'accordion')]"))
        )
        faq_button.click()
        time.sleep(4)

        expanded = faq_button.get_attribute("aria-expanded")
        self.assertEqual(expanded, "true")

    def test_case_019_positive_apple_arcade(self):
        driver = self.driver
        print("Test Case 019 - FAQ accessibility with keyboard")

        driver.get("https://www.apple.com/apple-arcade/")

        # Scroll to FAQ section
        faq_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)
        time.sleep(1)

        # Focus body
        body = driver.find_element(By.TAG_NAME, "body")
        ActionChains(driver).move_to_element(body).click().perform()
        time.sleep(1)

        # Try up to 10 TAB presses to find a FAQ button
        focused = None
        aria_controls = None
        for _ in range(10):
            ActionChains(driver).send_keys(Keys.TAB).perform()
            time.sleep(0.5)
            focused = driver.switch_to.active_element
            aria_controls = focused.get_attribute("aria-controls")
            if aria_controls:
                break  # Found a FAQ button

        self.assertIsNotNone(aria_controls, "Focused element is not a FAQ toggle button after 10 TABs")

        # Press ENTER to expand it
        focused.send_keys(Keys.ENTER)
        time.sleep(1)

        # Re-find the same button and check if it's expanded
        refreshed_faq_button = driver.find_element(By.XPATH, f"//button[@aria-controls='{aria_controls}']")
        expanded = refreshed_faq_button.get_attribute("aria-expanded")
        self.assertEqual(expanded, "true", "Focused FAQ item did not expand after ENTER key")

    def test_case_020_positive_apple_arcade(self):
        # Verify video banner playback
        driver = self.driver
        print("Test Case 020 - Verify video banner playback")

        driver.get("https://www.apple.com/apple-arcade/")

        wait = WebDriverWait(driver, 15)

        # Wait for the video element
        video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))

        # Try to find and click the pause button
        try:
            pause_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='pause hero video']")
            ))
            pause_button.click()
            time.sleep(2)

            # Check that video is paused
            is_paused = driver.execute_script("return arguments[0].paused;", video)
            self.assertTrue(is_paused, "Video did not pause after clicking Pause button")
        except TimeoutException:
            # If pause button not found, check if video is already paused
            is_paused = driver.execute_script("return arguments[0].paused;", video)
            if not is_paused:
                self.fail("Pause button not found and video is playing")

        # Find the play button and click it
        play_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='play hero video']")
        ))
        play_button.click()
        time.sleep(3)

        # Verify that video is playing
        is_playing = driver.execute_script("return !arguments[0].paused;", video)
        self.assertTrue(is_playing, "Video did not start playing after clicking Play button")

    def tearDown(self):
        self.driver.quit()

class EdgePositiveTests(unittest.TestCase):
    def setUp(self):
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=service, options=options)

    def test_case_016_positive_apple_arcade(self):
        # Verify "Try it free" button works
        driver = self.driver
        print("Test Case 016 - try free button")

        driver.get("https://www.apple.com/apple-arcade/")

        try_it_free = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Try it free')]"))
        )
        try_it_free.click()
        time.sleep(2)

        current_url = driver.current_url.lower()
        self.assertTrue("apple.com" in current_url or "apps.apple.com" in current_url)

    def test_case_017_positive_apple_arcade(self):
        # Verify external App Store links work
        driver = self.driver
        print("Test Case 017 - external App Store links")

        driver.get("https://www.apple.com/apple-arcade/")

        # Wait for the first App Store link to be present
        game_card = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'apps.apple.com')]"))
        )
        # Scroll to the App Store link smoothly and center it in the viewport
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", game_card)
        time.sleep(2)

        # Click the App Store link
        game_card.click()
        time.sleep(2)

        # Switch to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])

        # Verify that the current URL contains 'apps.apple.com'
        current_url = driver.current_url.lower()
        self.assertIn("apps.apple.com", current_url)

    def test_case_018_positive_apple_arcade(self):
        # Verify FAQ item expands on click
        driver = self.driver
        print("Test Case 018 - FAQ expand on click")

        driver.get("https://www.apple.com/apple-arcade/")

        # Scroll to the FAQ section header
        faq_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)
        time.sleep(2)

        faq_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-controls, 'accordion')]"))
        )
        faq_button.click()
        time.sleep(4)

        expanded = faq_button.get_attribute("aria-expanded")
        self.assertEqual(expanded, "true")

    def test_case_019_positive_apple_arcade(self):
        driver = self.driver
        print("Test Case 019 - FAQ accessibility with keyboard")

        driver.get("https://www.apple.com/apple-arcade/")

        # Locate the FAQ section header by XPath
        faq_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )

        # Scroll to the FAQ header to bring FAQ into view
        driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)
        time.sleep(1)

        # Focus on the body element
        body = driver.find_element(By.TAG_NAME, "body")

        # Press TAB once - focus should move to the first FAQ toggle button
        body.send_keys(Keys.TAB)
        time.sleep(1)

        # Get the currently focused element (expected first FAQ button)
        focused = driver.switch_to.active_element

        # Store unique attribute to refind the element later
        aria_controls = focused.get_attribute("aria-controls")

        # Press ENTER to expand the FAQ item
        focused.send_keys(Keys.ENTER)
        time.sleep(1)

        # Re-find the FAQ button after DOM update
        refreshed_faq_button = driver.find_element(By.XPATH, f"//button[@aria-controls='{aria_controls}']")

        # Verify that the FAQ item expanded (aria-expanded="true")
        expanded = refreshed_faq_button.get_attribute("aria-expanded")
        self.assertEqual(expanded, "true", "FAQ item did not expand after ENTER key")

    def test_case_020_positive_apple_arcade(self):
        # Verify video banner playback
        driver = self.driver
        print("Test Case 020 - Verify video banner playback")

        driver.get("https://www.apple.com/apple-arcade/")

        wait = WebDriverWait(driver, 15)

        # Wait for the video element
        video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))

        # Try to find and click the pause button
        try:
            pause_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='pause hero video']")
            ))
            pause_button.click()
            time.sleep(2)

            # Check that video is paused
            is_paused = driver.execute_script("return arguments[0].paused;", video)
            self.assertTrue(is_paused, "Video did not pause after clicking Pause button")
        except TimeoutException:
            # If pause button not found, check if video is already paused
            is_paused = driver.execute_script("return arguments[0].paused;", video)
            if not is_paused:
                self.fail("Pause button not found and video is playing")

        # Find the play button and click it
        play_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='play hero video']")
        ))
        play_button.click()
        time.sleep(3)

        # Verify that video is playing
        is_playing = driver.execute_script("return !arguments[0].paused;", video)
        self.assertTrue(is_playing, "Video did not start playing after clicking Play button")

    def tearDown(self):
        self.driver.quit()

class ChromeNegativeTestCases(unittest.TestCase):
    def setUp(self):
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=options)

    def scroll_to_faq(self):
        faq_header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_header
        )
        time.sleep(2)

    def test_case_016_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.scroll_to_faq()

        faq_button_xpath = "//button[contains(@aria-controls, 'accordion')]"
        initial_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, faq_button_xpath))
        )
        initial_state = initial_button.get_attribute("aria-expanded")

        states = []

        for i in range(10):
            try:
                button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, faq_button_xpath))
                )
                button.click()
                time.sleep(0.5)
                new_state = button.get_attribute("aria-expanded")
                states.append(new_state)
            except Exception as e:
                print(f"Click {i + 1} failed: {e}")
                states.append("error")

        print("Aria states after clicks:", states)

        self.assertIn("true", states, "aria-expanded did not become 'true' during 10 clicks")
        self.assertNotEqual(len(set(states)), 1, "aria-expanded remained the same after 10 clicks")

    def test_case_017_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        time.sleep(3)

        driver.set_window_size(300, 500)
        time.sleep(1)

        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", footer
        )
        time.sleep(5)

    def test_case_018_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        faq_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-controls, 'accordion')]"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_button
        )
        time.sleep(2)

        answer_id = faq_button.get_attribute("aria-controls")
        driver.execute_script(f"document.getElementById('{answer_id}').innerHTML = '';")
        time.sleep(2)

        faq_button.click()
        time.sleep(2)
        faq_button.click()
        time.sleep(2)
        faq_button.click()
        time.sleep(2)

    def test_case_019_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        driver.delete_all_cookies()
        cookies = driver.get_cookies()
        self.assertEqual(len(cookies), 0, f"Expected 0 cookies after deletion, but got {len(cookies)}")
        driver.refresh()

        wait = WebDriverWait(driver, 10)
        try_it_free_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Try it free')]"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", try_it_free_button
        )
        time.sleep(1)

        try_it_free_button.click()
        time.sleep(5)

    def test_case_020_negative_apple_arcade(self):
        self.driver.quit()
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.javascript": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=options)

        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.scroll_to_faq()

        faq_button = driver.find_element(By.XPATH, "//button[contains(@aria-controls, 'accordion')]")

        initial_state = faq_button.get_attribute("aria-expanded")

        answer_id = faq_button.get_attribute("aria-controls")
        answer_element = driver.find_element(By.ID, answer_id)
        self.assertTrue(answer_element.is_displayed(), "Answer should be visible initially with JS disabled")

        for _ in range(5):
            faq_button.click()
            time.sleep(0.3)

        final_state = faq_button.get_attribute("aria-expanded")
        self.assertEqual(final_state, initial_state, "aria-expanded attribute should not change when JS is disabled")
        self.assertTrue(answer_element.is_displayed(), "Answer should remain visible after clicks with JS disabled")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

class FirefoxNegativeTestCases(unittest.TestCase):
    def setUp(self):
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Firefox(service=service, options=options)

    def scroll_to_faq(self):
        faq_header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_header
        )
        time.sleep(2)

    def test_case_016_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.scroll_to_faq()

        faq_button_xpath = "//button[contains(@aria-controls, 'accordion')]"
        initial_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, faq_button_xpath))
        )
        initial_state = initial_button.get_attribute("aria-expanded")

        states = []

        for i in range(10):
            try:
                button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, faq_button_xpath))
                )
                button.click()
                time.sleep(0.5)
                new_state = button.get_attribute("aria-expanded")
                states.append(new_state)
            except Exception as e:
                print(f"Click {i + 1} failed: {e}")
                states.append("error")

        print("Aria states after clicks:", states)

        self.assertIn("true", states, "aria-expanded did not become 'true' during 10 clicks")
        self.assertNotEqual(len(set(states)), 1, "aria-expanded remained the same after 10 clicks")

    def test_case_017_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        time.sleep(3)

        driver.set_window_size(300, 500)
        time.sleep(1)

        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", footer
        )
        time.sleep(5)

    def test_case_018_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        faq_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-controls, 'accordion')]"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_button
        )
        time.sleep(2)

        answer_id = faq_button.get_attribute("aria-controls")
        driver.execute_script(f"document.getElementById('{answer_id}').innerHTML = '';")
        time.sleep(2)

        faq_button.click()
        time.sleep(2)
        faq_button.click()
        time.sleep(2)
        faq_button.click()
        time.sleep(2)

    def test_case_019_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        driver.delete_all_cookies()
        cookies = driver.get_cookies()
        self.assertEqual(len(cookies), 0, f"Expected 0 cookies after deletion, but got {len(cookies)}")
        driver.refresh()

        wait = WebDriverWait(driver, 10)
        try_it_free_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Try it free')]"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", try_it_free_button
        )
        time.sleep(1)

        try_it_free_button.click()
        time.sleep(5)

    def test_case_020_negative_apple_arcade(self):
        self.driver.quit()
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.set_preference("javascript.enabled", False)
        options.add_argument("--start-maximized")
        self.driver = webdriver.Firefox(service=service, options=options)

        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.scroll_to_faq()

        faq_button = driver.find_element(By.XPATH, "//button[contains(@aria-controls, 'accordion')]")

        initial_state = faq_button.get_attribute("aria-expanded")

        answer_id = faq_button.get_attribute("aria-controls")
        answer_element = driver.find_element(By.ID, answer_id)
        self.assertTrue(answer_element.is_displayed(), "Answer should be visible initially with JS disabled")

        for _ in range(5):
            faq_button.click()
            time.sleep(0.3)

        final_state = faq_button.get_attribute("aria-expanded")
        self.assertEqual(final_state, initial_state, "aria-expanded attribute should not change when JS is disabled")
        self.assertTrue(answer_element.is_displayed(), "Answer should remain visible after clicks with JS disabled")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

class EdgeNegativeTestCases(unittest.TestCase):
    def setUp(self):
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=service, options=options)

    def scroll_to_faq(self):
        faq_header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Questions? Answers.')]"))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_header
        )
        time.sleep(2)

    def test_case_016_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.scroll_to_faq()

        faq_button_xpath = "//button[contains(@aria-controls, 'accordion')]"
        initial_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, faq_button_xpath))
        )
        initial_state = initial_button.get_attribute("aria-expanded")

        states = []

        for i in range(10):
            try:
                button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, faq_button_xpath))
                )
                button.click()
                time.sleep(0.5)
                new_state = button.get_attribute("aria-expanded")
                states.append(new_state)
            except Exception as e:
                print(f"Click {i + 1} failed: {e}")
                states.append("error")

        print("Aria states after clicks:", states)


        self.assertIn("true", states, "aria-expanded did not become 'true' during 10 clicks")
        self.assertNotEqual(len(set(states)), 1, "aria-expanded remained the same after 10 clicks")

    def test_case_017_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        time.sleep(3)

        driver.set_window_size(300, 500)
        time.sleep(1)

        footer = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", footer
        )
        time.sleep(5)

    def test_case_018_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        faq_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-controls, 'accordion')]"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_button
        )
        time.sleep(2)

        answer_id = faq_button.get_attribute("aria-controls")
        driver.execute_script(f"document.getElementById('{answer_id}').innerHTML = '';")
        time.sleep(2)

        faq_button.click()
        time.sleep(2)
        faq_button.click()
        time.sleep(2)
        faq_button.click()
        time.sleep(2)

    def test_case_019_negative_apple_arcade(self):
        driver = self.driver
        driver.get("https://www.apple.com/apple-arcade/")
        driver.delete_all_cookies()
        cookies = driver.get_cookies()
        self.assertEqual(len(cookies), 0, f"Expected 0 cookies after deletion, but got {len(cookies)}")
        driver.refresh()

        wait = WebDriverWait(driver, 10)
        try_it_free_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Try it free')]"))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", try_it_free_button
        )
        time.sleep(1)

        try_it_free_button.click()
        time.sleep(5)

    def test_case_020_negative_apple_arcade(self):
        # Edge JS disable not trivial, skipping or separate config needed
        pass

    def tearDown(self):
        self.driver.quit()


#if __name__ == "__main__":
    #unittest.main(AllureReports)


#if __name__ == '__main__':
 #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))