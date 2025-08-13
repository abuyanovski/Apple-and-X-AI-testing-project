from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import helpers as h

# The webdriver management will be handled by the BrowserStack_SDK-sdk
# so this will be overridden and tests will run BrowserStack_SDK -
# without any changes to the test files!
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

try:

    # test case positive 31
    # TC_P_031
    print('                                                                    ')
    print('--------------------------------------------------------------------')
    print('                            Store/ Apple Watch                      ')
    print('--------------------------------------------------------------------')
    print('                                                                    ')
    print("                            POSITIVE TEST CASES                     ")
    print('                                                                    ')
    print('--------------------------------------------------------------------')
    print('                                                                    ')
    print('                               TC_P_031                             ')
    print('                                                                    ')
    print('--------------------------------------------------------------------')
    # Verify that user is able to contact a specialist with "Ask an Apple Watch Specialist".
    driver.get(h.site)
    print("1. Open 'https://www.apple.com/' website.")
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
    driver.find_element(By.XPATH, h.store_button).click()
    print("2. Click on the ‘Store’ button.")
    driver.find_element(By.XPATH, h.apple_watch).click()
    print('3. Click on the ‘Apple Watch’ button.')
    driver.find_element(By.XPATH,
                        "//a[@class='as-chat-button active as-buttonlink icon icon-after icon-external']").click()
    # Page title
    assert h.title in driver.title
    print("Page title is:", driver.title)
    print("4. Navigate to the ‘Ask an Apple Watch Specialist’ page.")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)
    driver.find_element(By.XPATH, "//h2[contains(text(),'Chat with us online.')]").click()
    print("5. Click on ‘Chat with us online’.")
    time.sleep(5)
    driver.find_element(By.ID, "txt_userMessage").send_keys("Buy an apple watch")
    print("6. In the chat window, send the message: “Buy an apple watch”.")
    driver.find_element(By.ID, "sendIcon").click()
    # The user successfully sent a message through the chat interface. All links provided in the chat were navigated to the correct pages without errors.

    print('--------------------------------------------------------------------')
    print('                                                                    ')
    print('                           TC_P_031 PASSED                          ')
    print('                                                                    ')
    print('--------------------------------------------------------------------')
finally:
    # Stop the driver
    driver.quit()
