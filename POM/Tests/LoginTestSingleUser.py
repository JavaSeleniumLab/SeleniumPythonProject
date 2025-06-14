import time
import pytest
from POM.Pages.LoginPage import LoginPage
from POM.Pages.InventoryPage import check_number_of_items, add_all_inventory_items, \
    check_number_of_items_in_shopping_cart, add_number_of_items_passed_by_user, remove_added_items_passed_by_user
from Fixture.FixtureSetUp import driver


def test_login_one_user(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    check_number_of_items(driver)
    add_number_of_items_passed_by_user(driver, 4)
    check_number_of_items_in_shopping_cart(driver,4)
    remove_added_items_passed_by_user(driver,3)
    check_number_of_items_in_shopping_cart(driver, 1)

