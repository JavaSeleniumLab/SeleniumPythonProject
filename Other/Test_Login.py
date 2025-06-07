from _pytest import unittest
from selenium import webdriver

def func(x):
    return x+1

class TestLoginPage:

    def test_1(self):
        assert func(2) == 3


    def test_2(self):
        assert func(3) == 3


    def test_3(self):
        assert func(4) == 5