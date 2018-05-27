# coding=utf-8
from selenium import webdriver


class BasePage(object):
    """
    basic page for inherit
    """

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
