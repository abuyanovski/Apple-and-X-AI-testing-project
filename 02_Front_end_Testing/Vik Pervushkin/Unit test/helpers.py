import string
import time
import random
from pkgutil import extend_path

import self
from IPython.utils.coloransi import value
from selenium.common import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.common import WebDriverException as WDE
from faker import Faker




# action with elements
def wait_for_element(driver, by, value, timeout=10):
    try:
        wait = WebDriverWait(driver, timeout)
        element = wait.until(
            EC.presence_of_element_located((by, value)),
            message=f"Element with locator '{value}' not found within {timeout} seconds"
        )
        print(f"Element located successfully: {value}")
        return element

    except TimeoutException:
        raise AssertionError(f"Timed out waiting for element: {value}")

    except Exception as e:
        raise AssertionError(f"Unexpected error while waiting for element '{value}': {e}")

def hover_over_element(driver, by, value, timeout):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value)),
            message=f"Element '{value}' was not visible within {timeout} seconds"
        )

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center' });", element)

        # Optional: Add small delay before hover
        time.sleep(1)

        # Perform hover
        actions = ActionChains(driver)
        actions.move_to_element(element).pause(2).perform()

        # Optional: Small delay to observe effect
        time.sleep(1)

        print(f"Successfully hovered over element with locator: {value}")
        return True

    except TimeoutException:
        print(f"Timed out waiting for element to be visible: {value}")
        return False

    except NoSuchElementException:
        print(f"Element not found: {value}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred while hovering over '{value}': {e}")
        return False

def hover_and_wait(driver, hover_locator, target_locator,timeout):
    start_time = time.time()
    #creating a loop until timeout is reached
    while time.time() - start_time < timeout:
        try:
            #hover again
            hover_element = driver.find_element(*hover_locator)
            ActionChains(driver).move_to_element(hover_element).pause(1).perform()
            print(f"Found and hovered over {hover_element}")

            #check if target element is visible
            elem = driver.find_element(*target_locator)
            if elem.is_displayed():
                print(f"Element {target_locator} found!")
                return True

        except:
            time.sleep(0.5)

    print("Timed out waiting for element.")
    return False


def hover_and_wait_for_submenu(driver, hover_locator, submenu_locator, timeout=10):
    #locating the element to hover
    hover_element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(hover_locator),
        message="Could not locate Support menu."
    )

    #scroll into a view
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center' });", hover_element)

    #hover over with a fat pause
    ActionChains(driver).move_to_element(hover_element).pause(5).perform()
    print(f"Hovered over {hover_locator} menu.")

    #checking if submenu drops
    #tracking if submenu appears , once submenu appears I will get out of the loop/ control when loop stops
    submenu_appeared = False
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            submenu_item = driver.find_element(*submenu_locator)
            if submenu_item.is_displayed():
                print("Submenu appeared successfully.")
                print("Submenu item found:", submenu_item.text)
                driver.save_screenshot("Success.png")
                submenu_appeared = True
                return True
        except:
            time.sleep(0.5)

    if not submenu_appeared:
        print("Submenu did NOT appear within timeout.")
        driver.save_screenshot("hover_error_submenu_not_found.png")
        return False


def click_on_elem(driver, by, value, timeout):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value)),
                f"Element '{value}' not clickable within {timeout} seconds"
            )
            driver.execute_script("""
                        arguments[0].scrollIntoView({
                            behavior: 'smooth',
                            block: 'center'
                        });
                    """, element)

            element.click()

            print(f"Clicked on element: {value}")
            return True

        except TimeoutException:
            print(f"Timeout waiting for element to be clickable: {value}")
            return False

        except Exception as e:
            print(f"Error clicking element '{value}': {e}")
            return False

def hover_with_js(driver, by, locator, timeout):
    elem = driver.find_element(by, locator, timeout)
    driver.execute_script("""
            var ev = document.createEvent('MouseEvent');
            ev.initMouseEvent(
                'mouseover', 
                true /* bubble */, 
                true /* cancelable */, 
                window, 
                0, 
                0, 
                0, 
                0, 
                0, 
                false, 
                false, 
                false, 
                false, 
                null
            );
            arguments[0].dispatchEvent(ev);
        """, elem)
    print("Hovered using JavaScript")

def delay():
    time.sleep(random.randint(2, 4))

def click_and_check(driver, by, locator, testing_element, timeout):
    try:
        play_button = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        # get initial value
        testing_element = driver.find_element(by,testing_element)
        initial_value = testing_element.get_attribute("value")
        print(F"Initial value: {initial_value}")
        # click
        try:
            play_button.click()
            print("Button clicked normally")
        except NoSuchElementException:
            print("error locating the button")
        #have to wait until the value isn't equal to initial value
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: testing_element.get_attribute("value") != initial_value
            )
        except TimeoutException:
            print("Value didn't change after clicking ")
            return False

        new_value = testing_element.get_attribute("value")
        print(f"New value: {new_value}")

        #Compare and print result
        if new_value != initial_value:
            print("Value changed — video state updated")
        else:
            print("Value did not change — something went wrong")


    except Exception as e:
        print(f" Error during check: {e}")
        return False


def is_element_present(driver, by, value):
    try:
        driver.find_element(by, value)
        print(f"Element with locator {value} is present.")
        return True
    except NoSuchElementException:
        print(f"Element with locator {value} is not present.")
        return False

def scroll_down(driver, by, value, pause_duration=2, timeout=10):
    try:
        # wait for the element to be present in the DOM
        target_element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        driver.execute_script("""
                   arguments[0].scrollIntoView({
                       behavior: 'smooth',
                       block: 'center'
                   });
               """, target_element)

        #scroll the element into view using JavaScript
        #driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

        #pause to simulate scrolling completion or data entry
        time.sleep(pause_duration)

        #optionally, return the element for further interaction
        return target_element

    except Exception as e:
        print(f"An error occurred while scrolling to the element: {e}")
        raise



def switch_new_tab(driver, main_url, expected_url, timeout):

    #get all open window handles
    windows = driver.window_handles
    #check if there is more than one tab open
    if len(windows) > 1:
        # Switch to the new tab (second window handle)
        driver.switch_to.window(windows[-1])
        current_url = driver.current_url
        print(f"Switched to new tab. URL: {driver.current_url}")

        #wait and validate if URL  provided
        if expected_url:
            WebDriverWait(driver, timeout).until(EC.url_to_be(current_url),
            message=f"Expected URL '{current_url}' found in new tab")
            print("URL validated")
            driver.get(main_url)

        else:
            raise Exception("No new tab was opened.")



def enter_data(driver, by, value, data_to_enter, timeout):
    try:
        # wait til elements becomes visible
        elem = WebDriverWait(driver,timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        elem.click()
        #scroll into a view
        driver.execute_script("""
            arguments[0].scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            });
        """, elem)
        #clear field and enter any data
        elem.clear()
        #type data
        elem.send_keys(str(data_to_enter))
        time.sleep(3)
        elem.send_keys(Keys.ENTER)
        print(f"Entered data:{data_to_enter}")
        return True
        #to slow things down
    except Exception as e:
        print(f"Unexpected error while entering data: {e}")
        return False


def select_from_dropdown(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        element.send_keys(Keys.DOWN)
        time.sleep(3)
        element.send_keys(Keys.ENTER)
        print(f"Selected from: {xpath[:30]}...")  #shortened confirmation message
        return True
    except Exception as e:
        print(f"Error selecting from {xpath}: {e}")
        return False

def random_text(driver, by, value, length):
    try:
        text_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        text_field.click()
        letters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
        random_string = ''.join(random.choice(letters) for _ in range(length))
        text_field.send_keys(random_string)
        print(random_string)
    except Exception as e:
        print(f"an error occurred:{e}")

def check_url(driver, expected_url, timeout):
    try:
        WebDriverWait(driver,timeout).until(
            EC.url_to_be(expected_url)
        )
        print(f"URL matched: {driver.current_url}")
    except Exception:
        actual_url = driver.current_url
        raise AssertionError(f"URL mismatch! Expected: {expected_url}, Actual: {actual_url}")


def validate_search(driver, by, value, timeout):
    try:
        error_message = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        assert "Sorry, no matches were found." in error_message.text, \
          f"Expected error message not found. Got: '{error_message.text}'"

    except NoSuchElementException:
        print("No such element found")


def space_input(driver, by, value, space_count):
    try:
        field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        field.clear()
        for _ in range(space_count):
            field.send_keys(Keys.SPACE)
            # validating values and count
        final_value = field.get_attribute("value")
        assert len(final_value) == space_count, f"Expected {space_count} spaces, got {len(final_value)}"
        print(f" if  {space_count} spaces entered one at a time - test failed ")
        print(f"Amount of spaces entered: {space_count}")

    except Exception as e:
        print(f" Test failed: {str(e)}")
        driver.save_screenshot("space_test_failure.png")
        raise

def generate_long_string(length=1000):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def back_and_forward(driver, home_url, by, value):
    driver.get(home_url)
    time.sleep(2)
    second_tab = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((by, value))
    )
    second_tab.click()
    print("clicked on:", driver.title)
    print("Clicked on Support tab, now executing the loop")
    time.sleep(2)
    # for loops repeats code multiple times
    #using range to run the loop specific number of times in this case 12 times
    for i in range(1, 13):
        print(f"\nIteration {i}") # this string shows which loop cycle is being executed
        #back
        driver.back()
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            print("Back to:", driver.title)

            WebDriverWait(driver, 10).until(
                lambda d: d.current_url == home_url
            )
        except Exception as e:
            print("Error after going back:", str(e))
        #user delay
        time.sleep(2)
        #forward
        driver.forward()
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            print("Forward to:", driver.title)
        except Exception as e:
            print("Error after going forward:", str(e))
            # this code will run 12 times in this loop

def fake_logIn(driver, email_by, email_value, password_by, password_value, timeout):
    fake=Faker()

    #fake credentials
    fake_email = fake.email()
    fake_password = fake.password()
    try:
        #wait for email field and type fake email
        email_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((email_by, email_value))
        )
        print("Email field is clickable.")
        email_field.click()
        email_field.send_keys(fake_email)
        email_field.send_keys(Keys.ENTER)
        print(f"Entered fake email: {fake_email}")

        # wait for password field and type fake password
        password_field = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((password_by, password_value))
        )
        print("Password field is clickable")
        password_field.click()
        password_field.send_keys(fake_password)
        password_field.send_keys(Keys.ENTER)
        print(f"Entered fake password: {fake_password}")

        return fake_email, fake_password


    except TimeoutException:
        print("[ERROR] Timed out waiting for element.")
        driver.save_screenshot("timeout_error_login.png")
    except ElementClickInterceptedException:
        print("[ERROR] Click was intercepted by another element.")
        driver.save_screenshot("click_intercepted_error_login.png")
    except Exception as e:
        print(f"[ERROR] Unexpected error during login: {str(e)}")
        driver.save_screenshot("unexpected_error_login.png")

def close_overlay(driver, timeout=5):
    try:
        overlay = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow all cookies')]"))
        )
        overlay.click()
        print("Closed cookie banner")
    except:
        pass

def  switchTo_IframeBy_id(driver, iframe_id, timeout):

    """
    :param driver: webdriver
    :param iframe_id: id for iframe to switch to
    :param timeout: time to wait for an element to appear
    :return: return True if element appears, False otherwise
    """
    try:
        iframe= WebDriverWait(driver,timeout).until(
        EC.presence_of_element_located((By.XPATH, f"//iframe[@id='{iframe_id}']"))
        )
        driver.switch_to.frame(iframe)
        return True
    except Exception as e:
        print(f"Failed to switch to iframe with ID '{iframe_id}': {e}")
        return False























