#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/1914:23
# @Author:levin
# @File:base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        # 判断driver和url，如有则复用，没有就初始化创建driver
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9111"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        # 封装find_element方法
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        # 封装find_element方法
        return self._driver.find_elements(by, locator)

    def wait_tobe_click(self, locator, time=5):
        # 封装显示等待方法
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))