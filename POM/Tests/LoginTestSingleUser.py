import time

import pytest

from POM.Pages.LoginPage import LoginPage, accept_alert, if_alert_present, click_on_back_pack, check_number_of_items
from Fixture.FixtureSetUp import driver


def test_login_one_user(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    time.sleep(5)
    check_number_of_items(driver)
    click_on_back_pack(driver)
    time.sleep(5)

