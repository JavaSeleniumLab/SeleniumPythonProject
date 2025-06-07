import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print(driver.title)

driver.maximize_window()
time.sleep(5)
#driver.ex_wait(500000)
