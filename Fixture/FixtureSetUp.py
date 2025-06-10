import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="function")
def driver():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headed')
    # options.add_argument('--no-sandbox')
    #options.add_argument('--disable-gpu')
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver=webdriver.Edge(service=ChromeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    print(driver.title)
    yield driver
    driver.quit()
    return driver