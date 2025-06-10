from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located, alert_is_present
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Fixture.FixtureSetUp import driver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.userNameBox = driver.find_element(By.ID, "user-name")
        self.passwordBox = driver.find_element(By.ID, "password")
        self.loginButton = driver.find_element(By.ID, "login-button")


    def login(self, username, password):
        self.userNameBox.send_keys(username)
        self.passwordBox.send_keys(password)
        assert (self.loginButton.is_displayed())
        self.loginButton.click()
