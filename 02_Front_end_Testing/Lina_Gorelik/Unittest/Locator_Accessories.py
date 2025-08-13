import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait


t_url = "https://www.apple.com/"
t_url_2 = "https://www.apple.com/shop/accessoriem"
t_url_3 = "https://www.apple.com/shop/bag"
module = "//span[@class='globalnav-link-text-container'][contains(.,'Accessories')]"

def delay():
    time.sleep(random.randint(5, 8))

# Positive
def tc_p_046(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(5)
    # Click "Accessories" button
    driver.find_element(By.XPATH, module).click()
    print("Accessories button is clickable")
    time.sleep(8)
    # Ensure the "Accessories" page loads correctly
    driver.find_element(By.XPATH, "//a[@class='localnav-title']").is_displayed()
    print("The 'Accessories' page loads correctly")

    # Check Page URL
    try:
        assert "https://www.apple.com/shop/accessories/all" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("Accessories wrong url.png")

    # Scroll to the bottom of the page and verify all elements are visible
    map=driver.find_element(By.XPATH, "//a[contains(text(),'Site Map')]")
    driver.execute_script("arguments[0].scrollIntoView();", map)
    time.sleep(8)
    print("Scrolling to the bottom of the page...")
    print("Verifying visibility of elements at the bottom of the page...")
    time.sleep(8)
    try:
        # Example: Check for a footer element or other content at the bottom of the page
        wait = WebDriverWait(driver, 8)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))
        print("PASS: All elements of the page are visible.")
    except Exception as e:
        print("FAIL: Elements of the page are not visible: {e}")
    print("Positive TC-P-046 PASS")

#----------------------------------------------------------------------------------------------------------------------

def tc_p_047(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(5)
    # Click "Accessories" button
    driver.find_element(By.XPATH, module).click()
    print("Accessories button is clickable")
    time.sleep(8)
    # Ensure the "Accessories" page loads correctly
    driver.find_element(By.XPATH, "//a[@class='localnav-title']").is_displayed()
    print("The 'Accessories' page loads correctly")
    time.sleep(8)
    # Click "Apple Vision Pro" button
    driver.find_element(By.XPATH, "//span[@class='rf-browser-itemname small-8'][contains(.,'Apple Vision Pro')]").click()
    print("The 'Apple Vision Pro' button is clickable")
    time.sleep(8)
    # Ensure the "Apple Vision Pro" page loads correctly
    driver.find_element(By.XPATH, "//a[contains(@data-display-name,'Apple Vision Pro Accessories')]").is_displayed()
    print("The 'Apple Vision Pro' page loads correctly")

    # Check Page URL
    try:
        assert "https://www.apple.com/shop/vision/accessories" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("Accessories wrong url.png")
    print("Positive TC-P-047 PASS")

#-----------------------------------------------------------------------------------------------------------------------

def tc_p_048(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(5)
    # Click "Accessories" button
    driver.find_element(By.XPATH, module).click()
    print("Accessories button is clickable")
    time.sleep(8)
    # Ensure the "Accessories" page loads correctly
    driver.find_element(By.XPATH, "//a[@class='localnav-title']").is_displayed()
    print("The 'Accessories' page loads correctly")
    time.sleep(8)
    # Click "Shop Headphones and Speakers" button
    driver.find_element(By.XPATH, "//a[@href='/shop/accessories/all/headphones-speakers'][contains(.,'Shop Headphones and Speakers')]").click()
    print("The 'Shop Headphones and Speakers' button is clickable")
    time.sleep(8)
    # Ensure the "Headphones and Speakers" page loads correctly
    driver.find_element(By.XPATH, "//h1[contains(text(),'Headphones & Speakers')]").is_displayed()
    print("The 'Headphones and Speakers' page loads correctly")
    time.sleep(8)
    # Check Page URL
    try:
        assert "https://www.apple.com/shop/accessories/all/headphones-speakers" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("Headphones-speakers wrong url.png")
    time.sleep(8)
    try:
        # Example: Check for a footer element or other content at the bottom of the page
        wait = WebDriverWait(driver, 8)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))
        print("PASS: All elements of the page are visible.")
    except Exception as e:
        print("FAIL: Elements of the page are not visible: {e}")
    print("Positive TC-P-048 PASS")

#-----------------------------------------------------------------------------------------------------------------------

def tc_p_049(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(5)
    # Click "Accessories" button
    driver.find_element(By.XPATH, module).click()
    print("Accessories button is clickable")
    time.sleep(8)
    # Ensure the "Accessories" page loads correctly
    driver.find_element(By.XPATH, "//a[@class='localnav-title']").is_displayed()
    print("The 'Accessories' page loads correctly")
    time.sleep(8)
    # Click "Show more" button
    driver.find_element(By.XPATH, "//div[contains(text(),'Show more')]").click()
    print("The 'Show more' button is clickable")
    time.sleep(8)
    # Click "Beats by Dr. Dre" button
    driver.find_element(By.XPATH, "//span[@class='rf-browser-itemname small-8'][contains(.,'Beats by Dr. Dre')]").click()
    print("The 'Beats by Dr. Dre' button is clickable")
    time.sleep(8)
    # Ensure the "Beats by Dr. Dre" page loads correctly
    driver.find_element(By.XPATH, "//a[@href='/shop/accessories/all/beats-featured'][contains(.,'Beats by Dr. Dre')]").is_displayed()
    print("The 'Beats by Dr. Dre' page loads correctly")
    time.sleep(8)
    # Check Page URL
    try:
        assert "https://www.apple.com/shop/accessories/all/beats-featured" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("Beats-featured wrong url.png")
    time.sleep(8)
    try:
        # Example: Check for a footer element or other content at the bottom of the page
        wait = WebDriverWait(driver, 8)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))
        print("PASS: All elements of the page are visible.")
    except Exception as e:
        print("FAIL: Elements of the page are not visible: {e}")
    print("Positive TC-P-049 PASS")

#-----------------------------------------------------------------------------------------------------------------------

def tc_p_050(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(5)
    # Click "Accessories" button
    driver.find_element(By.XPATH, module).click()
    print("Accessories button is clickable")
    time.sleep(8)
    # Ensure the "Accessories" page loads correctly
    driver.find_element(By.XPATH, "//a[@class='localnav-title']").is_displayed()
    print("The 'Accessories' page loads correctly")
    time.sleep(8)
    # Click "Manage Your Apple Account" button
    driver.find_element(By.XPATH, "//a[contains(text(),'Manage Your Apple Account')]").click()
    print("The 'Manage Your Apple Account' button is clickable")
    time.sleep(8)
    # Ensure the "Apple Account" page loads correctly
    driver.find_element(By.XPATH, "//a[@href='/']").is_displayed()
    print("The 'Apple Account' page loads correctly")
    time.sleep(8)
    # Check Page URL
    try:
        assert "https://account.apple.com/" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("Apple wrong url.png")
    time.sleep(8)
    try:
        # Example: Check for a footer element or other content at the bottom of the page
        wait = WebDriverWait(driver, 8)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))
        print("PASS: All elements of the page are visible.")
    except Exception as e:
        print("FAIL: Elements of the page are not visible: {e}")
    print("Positive TC-P-050 PASS")

    #---------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------------------

# Negative
def tc_n_046(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(5)
    # Click "Accessories" button
    driver.find_element(By.XPATH, "//a[contains(@data-globalnav-item-name,'accessories')]").click()
    print("Accessories button is clickable")
    time.sleep(10)
    # Ensure the "Accessories" page loads correctly
    driver.find_element(By.XPATH, "//a[@class='localnav-title']").is_displayed()
    print("The 'Accessories' page loads correctly")
    # Check Page URL
    try:
        assert "https://www.apple.com/shop/accessories/all" in driver.current_url
        print("URL is correct", driver.current_url)
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("Accessories wrong url.png")
    time.sleep(10)
    # Scroll to the "Find the accessories you are looking for" bottom
    find = driver.find_element(By.XPATH, "//input[contains(@name,'search')]")
    # driver.execute_script("arguments[0].scrollIntoView();", find)
    print("Scrolling to the 'Find the accessories you are looking for' bottom")
    time.sleep(10)
     # Enter the special characters in the "Find the accessories you are looking for"
    find.click()
    find.send_keys("*&^%$#@")
    find.send_keys(Keys.ENTER)
    time.sleep(10)

    # An error message 400 should be displayed.
    driver.find_element(By.XPATH, "//h2[contains(text(),'HTTP ERROR 400 Ambiguous URI path encoding')]").is_displayed()
    print("HTTP ERROR 400 Ambiguous URI path encoding")
    print("Negative TC_N_046 PASS")

#-----------------------------------------------------------------------------------------------------------------------

def tc_n_047(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(7)
    # Click "Accessories" button
    driver.find_element(By.XPATH, module).click()
    print("Accessories button is clickable")
    time.sleep(12)

    driver.find_element(By.XPATH, "(//a[contains(.,'Apple Pencil (USB-C)')])[1]").location_once_scrolled_into_view

    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)

    time.sleep(12)
    # Scroll to the "Apple Pencil (USB-C)" bottom
    print("Scrolling to the Apple Pencil (USB-C)")


    time.sleep(12)
    # Click "Apple Pencil (USB-C)" button
    driver.find_element(By.XPATH, "(//a[contains(.,'Apple Pencil (USB-C)')])[1]").click()
    print("'Apple Pencil (USB-C)' button is clickable")

    time.sleep(12)
    # Click "Add to Bag" button
    driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()
    print("'Add to Bag' button is clickable")

    time.sleep(12)
    # Click "Check Out" button
    driver.find_element(By.XPATH, "//button[@id='shoppingCart.actions.checkoutOtherPayments']").click()
    print("'Check Out' button is clickable")

    time.sleep(12)
    # Click "Continue as Guest" button
    driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']")
    driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']").click()
    print("'Continue as Guest' button is clickable")

    time.sleep(12)
    # Click "Continue to Shipping Address" button
    driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']").click()
    print("'Continue to Shipping Address' button is clickable")

    time.sleep(12)
    # Scroll the "First Name" line
    FirstName = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.firstName']")
    driver.execute_script("arguments[0].scrollIntoView();", FirstName)
    time.sleep(12)
    # In the "First Name" line, enter the special symbol "#"
    FirstName.send_keys("#")

    time.sleep(12)
    # Scroll the "Last Name" line
    LastName = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.lastName']")
    driver.execute_script("arguments[0].scrollIntoView();", LastName)
    time.sleep(12)
    # In the "Last Name" line, enter the special symbol "#"
    LastName.send_keys("#")

    time.sleep(12)
    # Scroll the "Street Address" line
    StreetAddress = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.street']")
    driver.execute_script("arguments[0].scrollIntoView();", StreetAddress)
    time.sleep(12)
    # In the "Street Address" line, enter the number "0"
    StreetAddress.send_keys("0")

    time.sleep(12)
    # Scroll the "Apt, Suite, Building (Optional)" line
    Apt = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.street2']")
    driver.execute_script("arguments[0].scrollIntoView();", Apt)
    time.sleep(12)
    # In the "Apt, Suite, Building (Optional)" line, enter the number "0"
    Apt.send_keys("0")

    time.sleep(12)
    # Scroll the "Zip Code" line
    ZipCode = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.zipLookup.postalCode']")
    driver.execute_script("arguments[0].scrollIntoView();", ZipCode)
    time.sleep(12)
    # In the "Zip Code" line, enter the number "92009"
    ZipCode.send_keys("92009")

    time.sleep(12)
    # Scroll the "Email Address" line
    email = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressContactEmail.address.emailAddress']")
    driver.execute_script("arguments[0].scrollIntoView();", email)
    time.sleep(12)
    # In the "Email Address" line, enter the "a@gmail.com"
    email.send_keys("a@gmail.com")

    time.sleep(12)
    # Scroll the "Phone Number" line
    PhoneNumber = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressContactPhone.address.fullDaytimePhone']")
    driver.execute_script("arguments[0].scrollIntoView();", PhoneNumber)
    time.sleep(12)
    # In the "Phone Number" line, enter the all digits 0 "(000) 000-0000"
    PhoneNumber.send_keys("(000) 000-0000")

    time.sleep(12)
    # Click "Continue to Payment" button
    driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']").click()
    print("'Continue to Payment' button is clickable")

    time.sleep(12)
    # Click "Use Existing Address" button
    driver.find_element(By.XPATH, "//span[contains(text(),'Use Existing Address')]").click()
    print("'Use Existing Address' button is clickable")
    driver.save_screenshot("Accessories existing Address.png")

    time.sleep(12)
    # Click "Credit or Debit Card" button
    driver.find_element(By.XPATH, "//label[@id='checkout.billing.billingoptions.credit_label']").click()
    print("'Credit or Debit Card' button is clickable")
    wait = WebDriverWait(driver, 10)

    try:
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.cardNumber']")))
        print("Enter your card information", "TC_N_047 FAIL")
        driver.save_screenshot("saving Accessories the incorrect data.png")

    except AssertionError:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='checkout.shipping.addressSelector.newAddress.address.firstName_error']")))
        print(
        "Should appear the inscription 'Please enter a valid ...'.")
        print("Negative TC_N_047 PASS")

#-----------------------------------------------------------------------------------------------------------------------

def tc_n_048(driver):
    # Go to https://www.apple.com/
    driver.get(t_url)
    time.sleep(5)
    # Click "Accessories" button
    driver.find_element(By.XPATH, module).click()
    print("Accessories button is clickable")
    time.sleep(10)

    driver.find_element(By.XPATH, "(//a[contains(.,'Apple Pencil (USB-C)')])[1]").location_once_scrolled_into_view

    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)

    time.sleep(10)
    # Scroll to the "Apple Pencil (USB-C)" bottom
    print("Scrolling to the Apple Pencil (USB-C)")

    time.sleep(10)
    # Click "Apple Pencil (USB-C)" button
    driver.find_element(By.XPATH, "(//a[contains(.,'Apple Pencil (USB-C)')])[1]").click()
    print("'Apple Pencil (USB-C)' button is clickable")

    time.sleep(10)
    # Click "Add to Bag" button
    driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()
    print("'Add to Bag' button is clickable")

    time.sleep(10)
    # Click "Check Out" button
    driver.find_element(By.XPATH, "//button[@id='shoppingCart.actions.checkoutOtherPayments']").click()
    print("'Check Out' button is clickable")

    time.sleep(10)
    # Click "Continue as Guest" button
    driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']")
    driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']").click()
    print("'Continue as Guest' button is clickable")

    time.sleep(10)
    # Click "Continue to Shipping Address" button
    driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']").click()
    print("'Continue to Shipping Address' button is clickable")

    time.sleep(10)
    # Scroll the "First Name" line
    FirstName = driver.find_element(By.XPATH,
                                    "//input[@id='checkout.shipping.addressSelector.newAddress.address.firstName']")
    driver.execute_script("arguments[0].scrollIntoView();", FirstName)
    time.sleep(10)
    # In the "First Name" line, enter the special symbol "#"
    FirstName.send_keys("#")

    time.sleep(10)
    # Scroll the "Last Name" line
    LastName = driver.find_element(By.XPATH,
                                   "//input[@id='checkout.shipping.addressSelector.newAddress.address.lastName']")
    driver.execute_script("arguments[0].scrollIntoView();", LastName)
    time.sleep(10)
    # In the "Last Name" line, enter the special symbol "#"
    LastName.send_keys("#")

    time.sleep(10)
    # Scroll the "Street Address" line
    StreetAddress = driver.find_element(By.XPATH,
                                        "//input[@id='checkout.shipping.addressSelector.newAddress.address.street']")
    driver.execute_script("arguments[0].scrollIntoView();", StreetAddress)
    time.sleep(10)
    # In the "Street Address" line, enter the number "0"
    StreetAddress.send_keys("0")

    time.sleep(10)
    # Scroll the "Apt, Suite, Building (Optional)" line
    Apt = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.street2']")
    driver.execute_script("arguments[0].scrollIntoView();", Apt)
    time.sleep(10)
    # In the "Apt, Suite, Building (Optional)" line, enter the number "0"
    Apt.send_keys("0")

    time.sleep(10)
    # Scroll the "Zip Code" line
    ZipCode = driver.find_element(By.XPATH,
                                  "//input[@id='checkout.shipping.addressSelector.newAddress.address.zipLookup.postalCode']")
    driver.execute_script("arguments[0].scrollIntoView();", ZipCode)
    time.sleep(10)
    # In the "Zip Code" line, enter the number "92009"
    ZipCode.send_keys("92009")

    time.sleep(10)
    # Scroll the "Email Address" line
    email = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressContactEmail.address.emailAddress']")
    driver.execute_script("arguments[0].scrollIntoView();", email)
    time.sleep(10)
    # In the "Email Address" line, enter the "a@gmail.com"
    email.send_keys("abc#def@mail.com")

    time.sleep(10)
    # Scroll the "Phone Number" line
    PhoneNumber = driver.find_element(By.XPATH,
                                      "//input[@id='checkout.shipping.addressContactPhone.address.fullDaytimePhone']")
    driver.execute_script("arguments[0].scrollIntoView();", PhoneNumber)
    time.sleep(10)
    # In the "Phone Number" line, enter the all digits 0 "(000) 000-0000"
    PhoneNumber.send_keys("(000) 000-0000")

    time.sleep(10)
    # Click "Continue to Payment" button
    driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']").click()
    print("'Continue to Payment' button is not clickable")
    wait = WebDriverWait(driver, 10)

    try:
        assert wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Please enter a valid email address.')]")))
        print("Please enter a valid email address.", "TC_N_048 PASS")

    except AssertionError:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Use Existing Address')]")))
        print("'Use Existing Address' button is visible")
        print("Negative TC_N_048 FAIL")

#-----------------------------------------------------------------------------------------------------------------------

def tc_n_049(driver):
    # Try entering the wrong URL for the "Accessories" page
    driver.get(t_url_2)
    time.sleep(10)
    # Check Page URL
    try:
        assert "https://www.apple.com/shop/accessories" in driver.current_url
        print("URL is correct", driver.current_url)
        print("Negative TC-N-049 FAIL")
    except AssertionError:
        print("URL is NOT correct", driver.current_url)
        driver.save_screenshot("wrong 'Accessories' url.png")
        print("Negative TC-N-049 PASS")

#-----------------------------------------------------------------------------------------------------------------------

def tc_n_050(driver):
    # View checkout page with empty cart through URL
    driver.get(t_url_3)
    time.sleep(12)
    # The text "Your cart is empty" should appear.
    driver.find_element(By.XPATH, "//h1[contains(text(),'Your bag is empty.')]").is_displayed()
    print("Your bag is empty", "TC_N_050 PASS")
