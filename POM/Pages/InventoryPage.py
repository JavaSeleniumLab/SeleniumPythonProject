from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located, alert_is_present
from selenium.webdriver.common.by import By
from Fixture.FixtureSetUp import driver



inventoryItems = "//button[@class='btn btn_primary btn_small btn_inventory ']"
backPackButton = "//button[@data-test='add-to-cart-sauce-labs-backpack']"
numberOfItems = "//div[@class='inventory_list']/div"
shoppingCartNumberOfItems = "//a[@class='shopping_cart_link']/span"
#addItemPassedByIndex = f"//div[@class='inventory_list']/div[{0}]//button"


def accept_alert(driver, timeout = 5 ):
    try:
        # Wait for the alert to be present
        driver(driver, timeout).until(alert_is_present())
        alert = driver.switch_to.alert
        print("Alert detected:", alert.text)
        return alert
    except (NoAlertPresentException, TimeoutException):
        print("No alert present")
        return None

def if_alert_present(driver, timeout = 10 ):
    driver(driver, timeout).until(alert_is_present())
    if alert_is_present():
        alert = driver.switch_to.alert
        print("Alert detected:", alert.text)
        alert.accept()


def click_on_back_pack(driver):
    driver.find_element(By.XPATH,backPackButton ).click()


def add_all_inventory_items(driver):
    allList = driver.find_elements(By.XPATH, inventoryItems)
    for item in allList:
        item.click()


def check_number_of_items(driver):
    inventoryList =driver.find_elements(By.XPATH, numberOfItems )
    print("Current URL:", driver.current_url)
    print("Number of items found:", len(inventoryList))
    assert len(inventoryList) == 6, f"Expected 6 items, but found {len(inventoryList)}"


def check_number_of_items_in_shopping_cart(driver, number_to_check):
    shoppingCartNumberOfItemsInCart = driver.find_element(By.XPATH, shoppingCartNumberOfItems).text
    print(shoppingCartNumberOfItemsInCart, "@@@@@@@@@@@@")
    assert int(shoppingCartNumberOfItemsInCart) == number_to_check, (f"Expected {number_to_check} items, "
                                                                     f"but found {shoppingCartNumberOfItemsInCart}")

    return int(shoppingCartNumberOfItemsInCart)


def add_number_of_items_passed_by_user(driver, numberPassedByUser):
    for i in range(numberPassedByUser):  # 0 to 4
     driver.find_element(By.XPATH, f"//div[@class='inventory_list']/div[{i+1}]//button").click()
    actual_number_of_items = check_number_of_items_in_shopping_cart(driver, numberPassedByUser)
    assert numberPassedByUser == actual_number_of_items, (f"Expected {numberPassedByUser} items, "
                                                          f"but found {actual_number_of_items}")
