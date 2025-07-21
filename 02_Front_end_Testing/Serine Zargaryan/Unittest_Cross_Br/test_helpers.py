import random
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


class PageSelectors:
    """Central repository for all page selectors and locators"""

    # URL constants
    APPLE_ARCADE_URL = "https://www.apple.com/apple-arcade/"

    # Main page elements
    BODY_TAG = (By.TAG_NAME, "body")
    FOOTER_TAG = (By.TAG_NAME, "footer")
    VIDEO_TAG = (By.TAG_NAME, "video")

    # Button selectors
    TRY_IT_FREE_BUTTON = (By.XPATH, "//a[contains(text(), 'Try it free')]")
    FAQ_BUTTON = (By.XPATH, "//button[contains(@aria-controls, 'accordion')]")

    # FAQ section selectors
    FAQ_HEADER_PRIMARY = (By.XPATH, "//h2[contains(text(),'Questions? Answers.')]")
    FAQ_HEADER_ALTERNATIVE = (By.XPATH, "//*[contains(text(), 'Questions') or contains(text(), 'FAQ')]")

    # App Store links
    APP_STORE_LINK = (By.XPATH, "//a[contains(@href, 'apps.apple.com')]")

    # Video control buttons
    PAUSE_BUTTON = (By.XPATH, "//button[@aria-label='pause hero video']")
    PLAY_BUTTON = (By.XPATH, "//button[@aria-label='play hero video']")

    @staticmethod
    def get_video_control_button(action):
        """Get video control button selector for specific action"""
        return (By.XPATH, f"//button[@aria-label='{action} hero video']")

    @staticmethod
    def get_faq_button_by_aria_controls(aria_controls):
        """Get FAQ button selector by aria-controls attribute"""
        return (By.XPATH, f"//button[@aria-controls='{aria_controls}']")

    @staticmethod
    def get_element_by_id(element_id):
        """Get element selector by ID"""
        return (By.ID, element_id)


class WebDriverFactory:
    """Factory class for creating WebDriver instances with common configurations"""

    @staticmethod
    def create_chrome_driver(maximize=True, disable_js=False, custom_prefs=None):
        """Create Chrome WebDriver with specified options"""
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()

        if maximize:
            options.add_argument("--start-maximized")

        if disable_js:
            prefs = {"profile.managed_default_content_settings.javascript": 2}
            options.add_experimental_option("prefs", prefs)

        if custom_prefs:
            options.add_experimental_option("prefs", custom_prefs)

        return webdriver.Chrome(service=service, options=options)

    @staticmethod
    def create_firefox_driver(maximize=True, disable_js=False):
        """Create Firefox WebDriver with specified options"""
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()

        if maximize:
            options.add_argument("--start-maximized")

        if disable_js:
            options.set_preference("javascript.enabled", False)

        return webdriver.Firefox(service=service, options=options)

    @staticmethod
    def create_edge_driver(maximize=True, driver_path=r"C:\drivers_selenium\msedgedriver.exe"):
        """Create Edge WebDriver with specified options"""
        service = EdgeService(executable_path=driver_path)
        options = webdriver.EdgeOptions()

        if maximize:
            options.add_argument("--start-maximized")

        return webdriver.Edge(service=service, options=options)


class AppleArcadePageActions:
    """Helper class containing common actions for Apple Arcade page"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.selectors = PageSelectors()

    def navigate_to_apple_arcade(self):
        """Navigate to Apple Arcade page"""
        self.driver.get(self.selectors.APPLE_ARCADE_URL)

    def scroll_to_faq_section(self):
        """Scroll to FAQ section on the page with improved reliability"""
        try:
            # First try to find by the header text
            faq_header = self.wait.until(
                EC.presence_of_element_located(self.selectors.FAQ_HEADER_PRIMARY)
            )
            print("Found FAQ header, scrolling to it")

        except TimeoutException:
            # Alternative: try to find any FAQ-related element
            try:
                faq_header = self.wait.until(
                    EC.presence_of_element_located(self.selectors.FAQ_HEADER_ALTERNATIVE)
                )
                print("Found alternative FAQ element, scrolling to it")

            except TimeoutException:
                # Last resort: find FAQ button directly
                faq_header = self.wait.until(
                    EC.presence_of_element_located(self.selectors.FAQ_BUTTON)
                )
                print("Found FAQ button directly, scrolling to it")

        # Scroll to the FAQ section with some offset above
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});",
            faq_header
        )
        time.sleep(2)

        # Scroll up a bit to ensure FAQ buttons are in viewport and focusable
        self.driver.execute_script("window.scrollBy(0, -100);")
        time.sleep(1)

        print("Completed scrolling to FAQ section")

    def navigate_to_faq_section(self):
        """Navigate to Apple Arcade page and scroll to FAQ section - for Edge test fix"""
        self.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )
        time.sleep(2)
        self.scroll_to_faq_section()

    def scroll_to_element(self, element, block='center'):
        """Scroll to specific element with smooth scrolling"""
        self.driver.execute_script(
            f"arguments[0].scrollIntoView({{behavior: 'smooth', block: '{block}'}});", element
        )
        time.sleep(2)

    def find_try_it_free_button(self, timeout=10):
        """Find and return the 'Try it free' button"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.selectors.TRY_IT_FREE_BUTTON)
        )

    def find_app_store_link(self, timeout=10):
        """Find and return the first App Store link"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.selectors.APP_STORE_LINK)
        )

    def find_faq_button(self, timeout=10):
        """Find and return FAQ accordion button"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.selectors.FAQ_BUTTON)
        )

    def find_video_element(self, timeout=15):
        """Find and return video element"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.selectors.VIDEO_TAG)
        )

    def find_video_control_button(self, action, timeout=15):
        """Find video control button (play/pause)"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.selectors.get_video_control_button(action))
        )

    def switch_to_new_tab(self):
        """Switch to the newly opened tab"""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def clear_cookies(self):
        """Delete all cookies"""
        self.driver.delete_all_cookies()

    def get_current_url_lower(self):
        """Get current URL in lowercase"""
        return self.driver.current_url.lower()


class KeyboardNavigationHelper:
    """Helper class for keyboard navigation actions"""

    def __init__(self, driver):
        self.driver = driver
        self.selectors = PageSelectors()

    def focus_body_element(self):
        """Focus on the body element"""
        body = self.driver.find_element(*self.selectors.BODY_TAG)
        ActionChains(self.driver).move_to_element(body).click().perform()
        time.sleep(0.5)  # Small delay after clicking
        return body

    def tab_to_element(self, max_tabs=15):
        """
        Press TAB key repeatedly until an element with 'aria-controls' attribute is focused,
        or until max_tabs is reached.
        Returns tuple (focused_element, aria_controls_value) or (None, None) if not found.
        """
        print(f"Starting TAB navigation, will try up to {max_tabs} tabs")

        for i in range(max_tabs):
            # Send TAB key
            ActionChains(self.driver).send_keys(Keys.TAB).perform()
            time.sleep(0.5)  # Wait for focus to move

            # Get currently focused element
            try:
                focused = self.driver.switch_to.active_element
                aria_controls = focused.get_attribute("aria-controls")
                tag_name = focused.tag_name.lower()

                # Debug output
                print(f"TAB {i + 1}: Focused on {tag_name} element, aria-controls: {aria_controls}")

                # Check if this is our FAQ button
                if aria_controls and 'accordion' in aria_controls:
                    print(f"Found FAQ button after {i + 1} TAB presses!")
                    return focused, aria_controls

            except Exception as e:
                print(f"Error getting focused element on TAB {i + 1}: {e}")
                continue

        print(f"Could not find FAQ button after {max_tabs} TAB presses")
        return None, None

    def press_enter_on_element(self, element):
        """Press ENTER key on the specified element"""
        try:
            element.send_keys(Keys.ENTER)
            print("Pressed ENTER on focused element")
        except Exception as e:
            print(f"Error pressing ENTER: {e}")
            # Fallback: try using ActionChains
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def send_tab_to_body(self, body_element):
        """Send TAB key to body element"""
        body_element.send_keys(Keys.TAB)
        time.sleep(0.5)


class TestAssertionHelpers:
    """Helper class for common test assertions"""

    @staticmethod
    def assert_url_contains_apple_domains(test_case, url):
        """Assert that URL contains Apple domains"""
        test_case.assertTrue("apple.com" in url or "apps.apple.com" in url)

    @staticmethod
    def assert_url_contains_app_store(test_case, url):
        """Assert that URL contains App Store domain"""
        test_case.assertIn("apps.apple.com", url)

    @staticmethod
    def assert_element_expanded(test_case, element):
        """Assert that element has aria-expanded='true'"""
        expanded = element.get_attribute("aria-expanded")
        test_case.assertEqual(expanded, "true")

    @staticmethod
    def assert_video_paused(test_case, driver, video_element):
        """Assert that video is paused"""
        is_paused = driver.execute_script("return arguments[0].paused;", video_element)
        test_case.assertTrue(is_paused, "Video did not pause after clicking Pause button")

    @staticmethod
    def assert_video_playing(test_case, driver, video_element):
        """Assert that video is playing"""
        is_playing = driver.execute_script("return !arguments[0].paused;", video_element)
        test_case.assertTrue(is_playing, "Video did not start playing after clicking Play button")


class VideoTestHelper:
    """Helper class for video-related test actions"""

    def __init__(self, driver):
        self.driver = driver
        self.page_actions = AppleArcadePageActions(driver)

    def test_video_controls(self, test_case):
        """Test video pause and play functionality"""
        video = self.page_actions.find_video_element()

        # Try to find and click pause button
        try:
            pause_button = self.page_actions.find_video_control_button('pause')
            pause_button.click()
            time.sleep(2)
            TestAssertionHelpers.assert_video_paused(test_case, self.driver, video)
        except TimeoutException:
            # If pause button not found, check if video is already paused
            is_paused = self.driver.execute_script("return arguments[0].paused;", video)
            if not is_paused:
                test_case.fail("Pause button not found and video is playing")

        # Find play button and test playback
        play_button = self.page_actions.find_video_control_button('play')
        play_button.click()
        time.sleep(3)
        TestAssertionHelpers.assert_video_playing(test_case, self.driver, video)


class NegativeTestHelper:
    """Helper class for negative test scenarios"""

    def __init__(self, driver):
        self.driver = driver
        self.page_actions = AppleArcadePageActions(driver)
        self.selectors = PageSelectors()

    def test_multiple_faq_clicks(self, test_case, num_clicks=10):
        """Test multiple clicks on FAQ button and verify state changes"""
        initial_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.selectors.FAQ_BUTTON)
        )

        states = []
        for i in range(num_clicks):
            try:
                button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(self.selectors.FAQ_BUTTON)
                )
                button.click()
                time.sleep(0.5)
                new_state = button.get_attribute("aria-expanded")
                states.append(new_state)
            except Exception as e:
                print(f"Click {i + 1} failed: {e}")
                states.append("error")

        print("Aria states after clicks:", states)

        test_case.assertIn("true", states, "aria-expanded did not become 'true' during clicks")
        test_case.assertNotEqual(len(set(states)), 1, "aria-expanded remained the same after multiple clicks")

    def resize_window_and_scroll(self, width=300, height=500):
        """Resize window to small size and scroll to footer"""
        self.driver.set_window_size(width, height)
        time.sleep(1)

        footer = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.selectors.FOOTER_TAG)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'end'});", footer
        )
        time.sleep(5)

    def manipulate_faq_content(self):
        """Remove FAQ answer content using JavaScript"""
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(self.selectors.BODY_TAG))

        faq_button = wait.until(
            EC.element_to_be_clickable(self.selectors.FAQ_BUTTON)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", faq_button
        )
        time.sleep(2)

        answer_id = faq_button.get_attribute("aria-controls")
        self.driver.execute_script(f"document.getElementById('{answer_id}').innerHTML = '';")
        time.sleep(2)

        # Click multiple times
        for _ in range(3):
            faq_button.click()
            time.sleep(2)

    def test_without_cookies(self, test_case):
        """Test functionality after clearing all cookies"""
        self.page_actions.clear_cookies()
        cookies = self.driver.get_cookies()
        test_case.assertEqual(len(cookies), 0, f"Expected 0 cookies after deletion, but got {len(cookies)}")

        self.driver.refresh()

        try_it_free_button = self.page_actions.find_try_it_free_button()
        self.page_actions.scroll_to_element(try_it_free_button)
        time.sleep(1)

        try_it_free_button.click()
        time.sleep(5)

    def test_javascript_disabled_faq(self, test_case):
        """Test FAQ functionality with JavaScript disabled"""
        self.page_actions.scroll_to_faq_section()

        faq_button = self.driver.find_element(*self.selectors.FAQ_BUTTON)
        initial_state = faq_button.get_attribute("aria-expanded")

        answer_id = faq_button.get_attribute("aria-controls")
        answer_element = self.driver.find_element(*self.selectors.get_element_by_id(answer_id))
        test_case.assertTrue(answer_element.is_displayed(), "Answer should be visible initially with JS disabled")

        # Click multiple times
        for _ in range(5):
            faq_button.click()
            time.sleep(0.3)

        final_state = faq_button.get_attribute("aria-expanded")
        test_case.assertEqual(final_state, initial_state,
                              "aria-expanded attribute should not change when JS is disabled")
        test_case.assertTrue(answer_element.is_displayed(),
                             "Answer should remain visible after clicks with JS disabled")
        time.sleep(3)


def delay():
    """Random delay between 1-5 seconds"""
    time.sleep(random.randint(1, 5))