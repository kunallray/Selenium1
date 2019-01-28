from selenium import webdriver
import time
import unittest

from POMDemo.Pages.loginpage import LoginPage

from  POMDemo.Pages.homepage import HomePage





class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\kunal\\PycharmProjects\\Selenium\\Driver\\chromedriver.exe")

        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)


    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login=LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()


        homepage=HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()


        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")







