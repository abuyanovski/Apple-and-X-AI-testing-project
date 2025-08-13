import time
import unittest

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Import helpers (assuming they are in a separate test_helpers.py file)
from test_helpers import (
    WebDriverFactory,
    AppleArcadePageActions,
    KeyboardNavigationHelper,
    TestAssertionHelpers,
    VideoTestHelper,
    NegativeTestHelper,
    PageSelectors
)


class BaseAppleArcadeTest(unittest.TestCase):
    """Base class for all Apple Arcade tests"""

    def setUp(self):
        """Create driver and helpers before each test"""
        self.driver = self._create_driver()
        self.page_actions = AppleArcadePageActions(self.driver)
        self.keyboard_helper = KeyboardNavigationHelper(self.driver)
        self.video_helper = VideoTestHelper(self.driver)
        self.negative_helper = NegativeTestHelper(self.driver)
        self.selectors = PageSelectors()

    def _create_driver(self):
        """Must be overridden in subclasses to create browser-specific driver"""
        raise NotImplementedError("Subclasses must implement _create_driver method")

    def tearDown(self):
        """Quit the driver after each test to free resources"""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()


class ChromePositiveTests(BaseAppleArcadeTest):
    """Positive test cases for Chrome browser"""

    def _create_driver(self):
        """Create Chrome WebDriver instance"""
        return WebDriverFactory.create_chrome_driver()

    def test_case_016_try_it_free_button(self):
        """Verify 'Try it free' button functionality"""
        print("Test Case 016 - Try it free button functionality")
        self.page_actions.navigate_to_apple_arcade()

        # Find and click the 'Try it free' button
        try_it_free = self.page_actions.find_try_it_free_button()
        try_it_free.click()
        time.sleep(2)

        # Verify redirection to Apple domain
        current_url = self.page_actions.get_current_url_lower()
        TestAssertionHelpers.assert_url_contains_apple_domains(self, current_url)

    def test_case_017_app_store_links(self):
        """Verify external App Store links functionality"""
        print("Test Case 017 - External App Store links functionality")
        self.page_actions.navigate_to_apple_arcade()

        # Find and click App Store link
        game_card = self.page_actions.find_app_store_link()
        self.page_actions.scroll_to_element(game_card)
        game_card.click()
        time.sleep(2)

        # Switch to new tab and verify URL
        self.page_actions.switch_to_new_tab()
        current_url = self.page_actions.get_current_url_lower()
        TestAssertionHelpers.assert_url_contains_app_store(self, current_url)

    def test_case_018_faq_expand_click(self):
        """Verify FAQ item expands on click"""
        print("Test Case 018 - FAQ expand on click functionality")
        self.page_actions.navigate_to_apple_arcade()
        self.page_actions.scroll_to_faq_section()

        # Find and click FAQ button
        faq_button = self.page_actions.find_faq_button()
        faq_button.click()
        time.sleep(4)

        # Verify expansion state
        TestAssertionHelpers.assert_element_expanded(self, faq_button)

    def test_case_019_faq_keyboard_accessibility(self):
        """Verify FAQ accessibility with keyboard navigation using TAB and ENTER keys"""
        print("Test Case 019 - FAQ keyboard accessibility")

        # Navigate to Apple Arcade page
        self.page_actions.navigate_to_apple_arcade()

        # Wait for page to fully load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )
        time.sleep(2)  # Additional wait for dynamic content

        # Scroll to FAQ section first
        self.page_actions.scroll_to_faq_section()
        time.sleep(2)  # Wait after scrolling

        # Focus on body element to start keyboard navigation
        body = self.keyboard_helper.focus_body_element()
        time.sleep(1)

        # Use tab_to_element helper to find FAQ button
        focused, aria_controls = self.keyboard_helper.tab_to_element(max_tabs=15)

        # If first attempt fails, try scrolling more precisely and retry
        if aria_controls is None:
            print("First TAB attempt failed, trying to scroll more precisely to FAQ")
            try:
                # Find FAQ button to scroll to it more precisely
                faq_button = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(self.selectors.FAQ_BUTTON)
                )
                # Scroll directly to the FAQ button
                self.page_actions.scroll_to_element(faq_button, block='center')
                time.sleep(2)

                # Focus on body again and retry TAB navigation
                body = self.keyboard_helper.focus_body_element()
                time.sleep(1)

                # Retry with more TAB presses
                focused, aria_controls = self.keyboard_helper.tab_to_element(max_tabs=20)

            except TimeoutException:
                self.fail("Could not find FAQ button on the page")

        # Verify we found the FAQ toggle button
        self.assertIsNotNone(
            aria_controls,
            "Could not focus on FAQ toggle button after TAB navigation. "
            "Try increasing max_tabs or check page structure."
        )

        print(f"Successfully focused on FAQ button with aria-controls: {aria_controls}")

        # Press ENTER to expand FAQ
        self.keyboard_helper.press_enter_on_element(focused)
        time.sleep(2)  # Wait for animation

        # Re-find the FAQ button and verify it's expanded
        refreshed_faq_button = self.driver.find_element(
            *self.selectors.get_faq_button_by_aria_controls(aria_controls)
        )
        expanded = refreshed_faq_button.get_attribute("aria-expanded")

        self.assertEqual(
            expanded,
            "true",
            f"FAQ item did not expand after ENTER key. Current state: {expanded}"
        )

        print("FAQ keyboard accessibility test completed successfully")

    def test_case_020_video_banner_playback(self):
        """Verify video banner playback controls"""
        print("Test Case 020 - Video banner playback controls")
        self.page_actions.navigate_to_apple_arcade()

        # Test video controls using helper
        self.video_helper.test_video_controls(self)


class FirefoxPositiveTests(BaseAppleArcadeTest):
    """Positive test cases for Firefox browser"""

    def _create_driver(self):
        """Create Firefox WebDriver instance"""
        return WebDriverFactory.create_firefox_driver()

    def test_case_016_try_it_free_button(self):
        """Verify 'Try it free' button functionality"""
        print("Test Case 016 - Try it free button functionality")
        self.page_actions.navigate_to_apple_arcade()

        # Find and click the 'Try it free' button
        try_it_free = self.page_actions.find_try_it_free_button()
        try_it_free.click()
        time.sleep(2)

        # Verify redirection to Apple domain
        current_url = self.page_actions.get_current_url_lower()
        TestAssertionHelpers.assert_url_contains_apple_domains(self, current_url)

    def test_case_017_app_store_links(self):
        """Verify external App Store links functionality"""
        print("Test Case 017 - External App Store links functionality")
        self.page_actions.navigate_to_apple_arcade()

        # Find and click App Store link
        game_card = self.page_actions.find_app_store_link()
        self.page_actions.scroll_to_element(game_card)
        game_card.click()
        time.sleep(2)

        # Switch to new tab and verify URL
        self.page_actions.switch_to_new_tab()
        current_url = self.page_actions.get_current_url_lower()
        TestAssertionHelpers.assert_url_contains_app_store(self, current_url)

    def test_case_018_faq_expand_click(self):
        """Verify FAQ item expands on click"""
        print("Test Case 018 - FAQ expand on click functionality")
        self.page_actions.navigate_to_apple_arcade()
        self.page_actions.scroll_to_faq_section()

        # Find and click FAQ button
        faq_button = self.page_actions.find_faq_button()
        faq_button.click()
        time.sleep(4)

        # Verify expansion state
        TestAssertionHelpers.assert_element_expanded(self, faq_button)

    def test_case_019_faq_keyboard_accessibility(self):
        """Firefox variant of FAQ keyboard accessibility test"""
        print("Test Case 019 - FAQ keyboard accessibility")
        self.page_actions.navigate_to_apple_arcade()
        self.page_actions.scroll_to_faq_section()

        # Focus on body element and use TAB navigation
        body = self.keyboard_helper.focus_body_element()
        time.sleep(1)

        # Find FAQ button using keyboard navigation
        focused, aria_controls = self.keyboard_helper.tab_to_element()

        # Verify we found a FAQ toggle button
        self.assertIsNotNone(
            aria_controls,
            "Focused element is not a FAQ toggle button after multiple TABs"
        )

        # Press ENTER to expand FAQ
        self.keyboard_helper.press_enter_on_element(focused)
        time.sleep(1)

        # Verify expansion state
        refreshed_faq_button = self.driver.find_element(
            *self.selectors.get_faq_button_by_aria_controls(aria_controls)
        )
        TestAssertionHelpers.assert_element_expanded(self, refreshed_faq_button)

    def test_case_020_video_banner_playback(self):
        """Verify video banner playback controls"""
        print("Test Case 020 - Video banner playback controls")
        self.page_actions.navigate_to_apple_arcade()

        # Test video controls using helper
        self.video_helper.test_video_controls(self)


class EdgePositiveTests(BaseAppleArcadeTest):
    """Positive test cases for Edge browser"""

    def _create_driver(self):
        """Create Edge WebDriver instance"""
        return WebDriverFactory.create_edge_driver()

    def test_case_016_try_it_free_button(self):
        """Verify 'Try it free' button functionality"""
        print("Test Case 016 - Try it free button functionality")
        self.page_actions.navigate_to_apple_arcade()

        # Find and click the 'Try it free' button
        try_it_free = self.page_actions.find_try_it_free_button()
        try_it_free.click()
        time.sleep(2)

        # Verify redirection to Apple domain
        current_url = self.page_actions.get_current_url_lower()
        TestAssertionHelpers.assert_url_contains_apple_domains(self, current_url)

    def test_case_017_app_store_links(self):
        """Verify external App Store links functionality"""
        print("Test Case 017 - External App Store links functionality")
        self.page_actions.navigate_to_apple_arcade()

        # Find and click App Store link
        game_card = self.page_actions.find_app_store_link()
        self.page_actions.scroll_to_element(game_card)
        game_card.click()
        time.sleep(2)

        # Switch to new tab and verify URL
        self.page_actions.switch_to_new_tab()
        current_url = self.page_actions.get_current_url_lower()
        TestAssertionHelpers.assert_url_contains_app_store(self, current_url)

    def test_case_018_faq_expand_click(self):
        """Verify FAQ item expands on click"""
        print("Test Case 018 - FAQ expand on click functionality")

        # Navigate to Apple Arcade page and wait for load
        self.page_actions.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )
        self.page_actions.scroll_to_faq_section()

        # Find and click FAQ button
        faq_button = self.page_actions.find_faq_button()
        faq_button.click()
        time.sleep(4)

        # Verify expansion state
        TestAssertionHelpers.assert_element_expanded(self, faq_button)

    def test_case_019_faq_keyboard_accessibility(self):
        """Edge variant of FAQ keyboard accessibility test with improved reliability"""
        print("Test Case 019 - FAQ keyboard accessibility")

        # Navigate and wait for page load
        self.page_actions.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )
        time.sleep(2)

        # Scroll to FAQ section
        self.page_actions.scroll_to_faq_section()
        time.sleep(2)

        # Focus on body element
        body = self.keyboard_helper.focus_body_element()
        time.sleep(1)

        # Use improved tab_to_element method
        focused, aria_controls = self.keyboard_helper.tab_to_element(max_tabs=15)

        # If not found, try fallback approach
        if aria_controls is None:
            print("TAB navigation failed, trying single TAB as fallback")
            self.keyboard_helper.send_tab_to_body(body)
            time.sleep(1)
            focused = self.driver.switch_to.active_element
            aria_controls = focused.get_attribute("aria-controls")

        # Verify we found FAQ button
        self.assertIsNotNone(
            aria_controls,
            "Could not focus on FAQ toggle button with keyboard navigation"
        )

        # Press ENTER to expand FAQ
        self.keyboard_helper.press_enter_on_element(focused)
        time.sleep(2)

        # Verify expansion state
        refreshed_faq_button = self.driver.find_element(
            *self.selectors.get_faq_button_by_aria_controls(aria_controls)
        )
        TestAssertionHelpers.assert_element_expanded(self, refreshed_faq_button)

    def test_case_020_video_banner_playback(self):
        """Verify video banner playback controls"""
        print("Test Case 020 - Video banner playback controls")
        self.page_actions.navigate_to_apple_arcade()

        # Test video controls using helper
        self.video_helper.test_video_controls(self)


class ChromeNegativeTests(BaseAppleArcadeTest):
    """Negative test cases for Chrome browser"""

    def _create_driver(self):
        """Create Chrome WebDriver instance"""
        return WebDriverFactory.create_chrome_driver()

    def test_case_016_multiple_faq_clicks(self):
        """Test multiple FAQ clicks for state consistency"""
        print("Test Case 016 - Multiple FAQ clicks test")
        self.page_actions.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )
        self.page_actions.scroll_to_faq_section()

        # Use helper for multiple FAQ clicks test
        self.negative_helper.test_multiple_faq_clicks(self)

    def test_case_017_small_viewport_test(self):
        """Test functionality on small viewport"""
        print("Test Case 017 - Small viewport test")
        self.page_actions.navigate_to_apple_arcade()
        time.sleep(3)

        # Use helper for viewport resize and scroll test
        self.negative_helper.resize_window_and_scroll()

    def test_case_018_content_manipulation(self):
        """Test behavior after content manipulation"""
        print("Test Case 018 - Content manipulation test")
        self.page_actions.navigate_to_apple_arcade()

        # Use helper for content manipulation test
        self.negative_helper.manipulate_faq_content()

    def test_case_019_no_cookies_test(self):
        """Test functionality without cookies"""
        print("Test Case 019 - No cookies test")
        self.page_actions.navigate_to_apple_arcade()

        # Use helper for no cookies test
        self.negative_helper.test_without_cookies(self)

    def test_case_020_javascript_disabled(self):
        """Test functionality with JavaScript disabled"""
        print("Test Case 020 - JavaScript disabled test")

        # Recreate driver with JavaScript disabled
        self.driver.quit()
        self.driver = WebDriverFactory.create_chrome_driver(disable_js=True)
        self.page_actions = AppleArcadePageActions(self.driver)
        self.negative_helper = NegativeTestHelper(self.driver)

        # Navigate and wait for page load
        self.page_actions.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )

        # Test JavaScript disabled FAQ functionality
        self.negative_helper.test_javascript_disabled_faq(self)


class FirefoxNegativeTests(BaseAppleArcadeTest):
    """Negative test cases for Firefox browser"""

    def _create_driver(self):
        """Create Firefox WebDriver instance"""
        return WebDriverFactory.create_firefox_driver()

    def test_case_016_multiple_faq_clicks(self):
        """Test multiple FAQ clicks for state consistency"""
        print("Test Case 016 - Multiple FAQ clicks test")
        self.page_actions.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )
        self.page_actions.scroll_to_faq_section()

        # Use helper for multiple FAQ clicks test
        self.negative_helper.test_multiple_faq_clicks(self)

    def test_case_017_small_viewport_test(self):
        """Test functionality on small viewport"""
        print("Test Case 017 - Small viewport test")
        self.page_actions.navigate_to_apple_arcade()
        time.sleep(3)

        # Use helper for viewport resize and scroll test
        self.negative_helper.resize_window_and_scroll()

    def test_case_018_content_manipulation(self):
        """Test behavior after content manipulation"""
        print("Test Case 018 - Content manipulation test")
        self.page_actions.navigate_to_apple_arcade()

        # Use helper for content manipulation test
        self.negative_helper.manipulate_faq_content()

    def test_case_019_no_cookies_test(self):
        """Test functionality without cookies"""
        print("Test Case 019 - No cookies test")
        self.page_actions.navigate_to_apple_arcade()

        # Use helper for no cookies test
        self.negative_helper.test_without_cookies(self)

    def test_case_020_javascript_disabled(self):
        """Test functionality with JavaScript disabled"""
        print("Test Case 020 - JavaScript disabled test")

        # Recreate driver with JavaScript disabled
        self.driver.quit()
        self.driver = WebDriverFactory.create_firefox_driver(disable_js=True)
        self.page_actions = AppleArcadePageActions(self.driver)
        self.negative_helper = NegativeTestHelper(self.driver)

        # Navigate and wait for page load
        self.page_actions.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )

        # Test JavaScript disabled FAQ functionality
        self.negative_helper.test_javascript_disabled_faq(self)


class EdgeNegativeTests(BaseAppleArcadeTest):
    """Negative test cases for Edge browser"""

    def _create_driver(self):
        """Create Edge WebDriver instance"""
        return WebDriverFactory.create_edge_driver()

    def test_case_016_multiple_faq_clicks(self):
        """Test multiple FAQ clicks for state consistency"""
        print("Test Case 016 - Multiple FAQ clicks test")
        self.page_actions.navigate_to_apple_arcade()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.selectors.BODY_TAG)
        )
        self.page_actions.scroll_to_faq_section()

        # Use helper for multiple FAQ clicks test
        self.negative_helper.test_multiple_faq_clicks(self)

    def test_case_017_small_viewport_test(self):
        """Test functionality on small viewport"""
        print("Test Case 017 - Small viewport test")
        self.page_actions.navigate_to_apple_arcade()
        time.sleep(3)

        # Use helper for viewport resize and scroll test
        self.negative_helper.resize_window_and_scroll()

    def test_case_018_content_manipulation(self):
        """Test behavior after content manipulation"""
        print("Test Case 018 - Content manipulation test")
        self.page_actions.navigate_to_apple_arcade()

        # Use helper for content manipulation test
        self.negative_helper.manipulate_faq_content()

    def test_case_019_no_cookies_test(self):
        """Test functionality without cookies"""
        print("Test Case 019 - No cookies test")
        self.page_actions.navigate_to_apple_arcade()

        # Use helper for no cookies test
        self.negative_helper.test_without_cookies(self)

    def test_case_020_javascript_disabled(self):
        """Test functionality with JavaScript disabled (Edge - skipped)"""
        print("Test Case 020 - JavaScript disabled test (Edge - skipped)")
        # JavaScript disable test is not implemented for Edge yet
        pass


if __name__ == "__main__":
    # Run all test classes
    unittest.main()