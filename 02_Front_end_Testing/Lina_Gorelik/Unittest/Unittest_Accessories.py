import Locator_Accessories as lc
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
#import HtmlTestRunner
#import AllureReports


# driver sleep from 2 to 8 seconds
def delay():
    time.sleep(random.randint(2, 8))


class AllElement:
    pass


class WebElement:
    pass


class Sign:
    pass


class ChromePositiveAccessories(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Google website
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

# Positive
    # As per unittest module, individual test should start with test_
    def test_TC_P_046(self):
        driver = self.driver
        lc.tc_p_046(driver)
        driver.quit()


    def test_TC_P_047(self):
        driver = self.driver
        lc.tc_p_047(driver)
        driver.quit()


    def test_TC_P_048(self):
        driver = self.driver
        lc.tc_p_048(driver)
        driver.quit()


    def test_TC_P_049(self):
        driver = self.driver
        lc.tc_p_049(driver)
        driver.quit()


    def test_TC_P_050(self):
        driver = self.driver
        lc.tc_p_050(driver)
        driver.quit()

#_________________________________________________________________________________________________
#-------------------------------------------------------------------------------------------------


class ChromeNegativeAccessories(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Google website
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # Negative tests
    def test_TC_N_046(self):
        driver = self.driver
        lc.tc_n_046(driver)
        driver.quit()


    def test_TC_N_047(self):
        driver = self.driver
        lc.tc_n_047(driver)
        driver.quit()


    def test_TC_N_048(self):
        driver = self.driver
        lc.tc_n_048(driver)
        driver.quit()


    def test_TC_N_049(self):
        driver = self.driver
        lc.tc_n_049(driver)
        driver.quit()


    def test_TC_N_050(self):
        driver = self.driver
        lc.tc_n_050(driver)
        driver.quit()

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class FirefoxPositiveAccessories(unittest.TestCase):

    def setUp(self):

        # Next 3 lines of code is disabled Captcha in Firefox website
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

# Positive
    # As per unittest module, individual test should start with test_
    def test_TC_P_046(self):
        driver = self.driver
        lc.tc_p_046(driver)
        driver.quit()


    def test_TC_P_047(self):
        driver = self.driver
        lc.tc_p_047(driver)
        driver.quit()


    def test_TC_P_048(self):
        driver = self.driver
        lc.tc_p_048(driver)
        driver.quit()


    def test_TC_P_049(self):
        driver = self.driver
        lc.tc_p_049(driver)
        driver.quit()


    def test_TC_P_050(self):
        driver = self.driver
        lc.tc_p_050(driver)
        driver.quit()

# _________________________________________________________________________________________________
 # -------------------------------------------------------------------------------------------------

class FirefoxNegativeAccessories(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Firefox website
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()
        time.sleep(10)

# Negative tests
    # As per unittest module, individual test should start with test_
    def test_TC_N_046(self):
        driver = self.driver
        lc.tc_n_046(driver)
        driver.quit()


    def test_TC_N_047(self):
        driver = self.driver
        lc.tc_n_047(driver)
        driver.quit()


    def test_TC_N_048(self):
        driver = self.driver
        lc.tc_n_048(driver)
        driver.quit()


    def test_TC_N_049(self):
        driver = self.driver
        lc.tc_n_049(driver)
        driver.quit()


    def test_TC_N_050(self):
        driver = self.driver
        lc.tc_n_050(driver)
        driver.quit()

#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

class EdgePositiveAccessories(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Edge website
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # options.add_argument('--headless')
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()

# Positive
    # As per unittest module, individual test should start with test_
    def test_TC_P_046(self):
        driver = self.driver
        lc.tc_p_046(driver)
        driver.quit()

    def test_TC_P_047(self):
        driver = self.driver
        lc.tc_p_047(driver)
        driver.quit()

    def test_TC_P_048(self):
        driver = self.driver
        lc.tc_p_048(driver)
        driver.quit()

    def test_TC_P_049(self):
        driver = self.driver
        lc.tc_p_049(driver)
        driver.quit()

    def test_TC_P_050(self):
        driver = self.driver
        lc.tc_p_050(driver)
        driver.quit()

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class EdgeNegativeAccessories(unittest.TestCase):

    def setUp(self):
        # Next 3 lines of code is disabled Captcha in Edge website
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.page_load_strategy = 'eager'
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.")
        # options.add_argument('--headless')
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        self.driver.maximize_window()
        time.sleep(8)

# Negative tests
    # As per unittest module, individual test should start with test_
    def test_TC_N_046(self):
        driver = self.driver
        lc.tc_n_046(driver)
        driver.quit()


    def test_TC_N_047(self):
        driver = self.driver
        lc.tc_n_047(driver)
        driver.quit()


    def test_TC_N_048(self):
        driver = self.driver
        lc.tc_n_048(driver)
        driver.quit()


    def test_TC_N_049(self):
        driver = self.driver
        lc.tc_n_049(driver)
        driver.quit()


    def test_TC_N_050(self):
        driver = self.driver
        lc.tc_n_050(driver)
        driver.quit()


    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()

# # if __name__ == '__main__':
# #     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

# # if __name__ == "__main__":
# #    unittest.main(AllureReports)
