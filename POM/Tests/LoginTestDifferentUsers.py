import pytest

from POM.Pages.LoginPage import LoginPage
from POM.DriverSetUp import DriverSetUp

@pytest.mark.parametrize("username, password",[
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])


def test_login(username, password):
    login = LoginPage()
    login.login(username, password)

def test_login2():
    print("test_login")
