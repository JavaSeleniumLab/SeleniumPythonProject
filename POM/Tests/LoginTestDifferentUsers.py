import time
import pytest
from POM.Pages.LoginPage import LoginPage
from POM.Pages.InventoryPage import check_number_of_items, add_all_inventory_items, click_on_back_pack, \
    check_number_of_items_in_shopping_cart, add_number_of_items_passed_by_user, remove_added_items_passed_by_user
from Fixture.FixtureSetUp import driver

@pytest.mark.parametrize("username, password",[
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])

def test_login(driver,username, password):
    login = LoginPage(driver)
    login.login(username, password)
    check_number_of_items(driver)
    add_number_of_items_passed_by_user(driver, 5)
    check_number_of_items_in_shopping_cart(driver, 5)
    remove_added_items_passed_by_user(driver, 3)
    check_number_of_items_in_shopping_cart(driver, 2)


