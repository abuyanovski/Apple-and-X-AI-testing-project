from selenium import webdriver
import AllureReports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import unittest
import time
import Helpers_SpaceX_Starship as H
from selenium.webdriver.common.keys import Keys
from faker import Faker
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
fake = Faker()
def delay():
    time.sleep(random.randint(1, 4))
class ChromePositiveTests(unittest.TestCase):
    def setUp(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        # self.driver.set_window_size(1920, 1080)