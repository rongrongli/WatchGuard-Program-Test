#-*- coding:utf-8 -*-


class BasePage(object):
    """
    basic page for inherit
    """

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
