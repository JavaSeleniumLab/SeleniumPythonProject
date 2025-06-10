import time

import pytest

from POM.Pages.LoginPage import LoginPage, accept_alert, check_number_of_items, click_on_back_pack
from Fixture.FixtureSetUp import driver

@pytest.mark.parametrize("username, password",[
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])


def test_login(driver,username, password):
    login = LoginPage(driver)
    login.login(username, password)
    time.sleep(5)
    check_number_of_items(driver)
    click_on_back_pack(driver)


