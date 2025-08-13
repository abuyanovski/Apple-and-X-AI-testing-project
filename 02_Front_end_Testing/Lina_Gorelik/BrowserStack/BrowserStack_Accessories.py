import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait

def delay():
    time.sleep(random.randint(1, 30))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
# Go to https://www.apple.com/
driver.get("https://www.apple.com/")
# Click "Accessories" button
driver.find_element(By.XPATH, "//span[@class='globalnav-link-text-container'][contains(.,'Accessories')]").click()

print("Accessories button is clickable")

driver.find_element(By.XPATH, "(//a[contains(.,'Apple Pencil (USB-C)')])[1]").location_once_scrolled_into_view

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.SPACE)

time.sleep(5)
# Scroll to the "Apple Pencil (USB-C)" bottom
print("Scrolling to the Apple Pencil (USB-C)")


time.sleep(5)
# Click "Apple Pencil (USB-C)" button
driver.find_element(By.XPATH, "(//a[contains(.,'Apple Pencil (USB-C)')])[1]").click()
print("'Apple Pencil (USB-C)' button is clickable")

time.sleep(5)
# Click "Add to Bag" button
driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()
print("'Add to Bag' button is clickable")

time.sleep(5)
# Click "Check Out" button
driver.find_element(By.XPATH, "//button[@id='shoppingCart.actions.checkoutOtherPayments']").click()
print("'Check Out' button is clickable")

time.sleep(5)
# Click "Continue as Guest" button
driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']")
driver.find_element(By.XPATH, "//button[@id='signIn.guestLogin.guestLogin']").click()
print("'Continue as Guest' button is clickable")

time.sleep(10)
# Click "Continue to Shipping Address" button
driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']").click()
print("'Continue to Shipping Address' button is clickable")

time.sleep(3)
# Scroll the "First Name" line
FirstName = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.firstName']")
driver.execute_script("arguments[0].scrollIntoView();", FirstName)
time.sleep(3)
# In the "First Name" line, enter the special symbol "#"
FirstName.send_keys("#")

time.sleep(3)
# Scroll the "Last Name" line
LastName = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.lastName']")
driver.execute_script("arguments[0].scrollIntoView();", LastName)
time.sleep(3)
# In the "Last Name" line, enter the special symbol "#"
LastName.send_keys("#")

time.sleep(3)
# Scroll the "Street Address" line
StreetAddress = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.street']")
driver.execute_script("arguments[0].scrollIntoView();", StreetAddress)
time.sleep(3)
# In the "Street Address" line, enter the number "0"
StreetAddress.send_keys("0")

time.sleep(3)
# Scroll the "Apt, Suite, Building (Optional)" line
Apt = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.street2']")
driver.execute_script("arguments[0].scrollIntoView();", Apt)
time.sleep(3)
# In the "Apt, Suite, Building (Optional)" line, enter the number "0"
Apt.send_keys("0")

time.sleep(3)
# Scroll the "Zip Code" line
ZipCode = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressSelector.newAddress.address.zipLookup.postalCode']")
driver.execute_script("arguments[0].scrollIntoView();", ZipCode)
time.sleep(3)
# In the "Zip Code" line, enter the number "92009"
ZipCode.send_keys("92009")

time.sleep(3)
# Scroll the "Email Address" line
email = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressContactEmail.address.emailAddress']")
driver.execute_script("arguments[0].scrollIntoView();", email)
time.sleep(3)
# In the "Email Address" line, enter the "a@gmail.com"
email.send_keys("a@gmail.com")

time.sleep(3)
# Scroll the "Phone Number" line
PhoneNumber = driver.find_element(By.XPATH, "//input[@id='checkout.shipping.addressContactPhone.address.fullDaytimePhone']")
driver.execute_script("arguments[0].scrollIntoView();", PhoneNumber)
time.sleep(3)
# In the "Phone Number" line, enter the all digits 0 "(000) 000-0000"
PhoneNumber.send_keys("(000) 000-0000")

time.sleep(8)
# Click "Continue to Payment" button
driver.find_element(By.XPATH, "//button[@id='rs-checkout-continue-button-bottom']").click()
print("'Continue to Payment' button is clickable")

time.sleep(8)
# Click "Use Existing Address" button
driver.find_element(By.XPATH, "//span[contains(text(),'Use Existing Address')]").click()
print("'Use Existing Address' button is clickable")
driver.save_screenshot("Existing Address.png")

time.sleep(8)
# Click "Credit or Debit Card" button
driver.find_element(By.XPATH, "//label[@id='checkout.billing.billingoptions.credit_label']").click()
print("'Credit or Debit Card' button is clickable")
wait = WebDriverWait(driver, 10)

try:
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs.cardInput-0.cardNumber']")))
    print("Enter your card information", "TC_N_047 FAIL")
    driver.save_screenshot("saving the incorrect data.png")

except AssertionError:
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='checkout.shipping.addressSelector.newAddress.address.firstName_error']")))
    print(
        "Should appear the inscription 'Please enter a valid ...'.")
    print("Negative TC_N_047 PASS")

def tearDown(self):
    self.driver.quit()