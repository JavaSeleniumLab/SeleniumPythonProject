import pytest

from POM.Pages.LoginPage import LoginPage
from Fixture.FixtureSetUp import driver

@pytest.mark.parametrize("username, password",[
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])


def test_login(driver,username, password):
    login = LoginPage(driver)
    login.login(username, password)


