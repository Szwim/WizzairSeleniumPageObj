import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)

    def tearDown(self):
        self.driver.quit()
        print("Koniec testu")