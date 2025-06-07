from selenium.webdriver.common.by import By

from POM.DriverSetUp import DriverSetUp
from POM.DriverSetUp.DriverSetUp import *

class LoginPage:

    def __init__(self):
        driver = DriverSetUp.launch_browser()
        self.userNameBox = driver.find_element(By.ID, "user-name")
        self.passwordBox = driver.find_element(By.ID, "password")
        self.loginButton = driver.find_element(By.ID, "login-button")


    def login(self, username, password):
        self.userNameBox.send_keys(username)
        self.passwordBox.send_keys(password)
        self.loginButton.click()

