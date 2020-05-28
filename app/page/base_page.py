#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/259:05
# @Author:levin
# @File:base_page.py
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os


current_path = os.getcwd()


class BasePage:
    _black_list = [(By.XPATH, "//*[@text='确定']"),
                   (By.XPATH, "//*[@text='下次再说']"),
                   (By.XPATH, "//*[@text='跳过']")
                   ]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        # 定位元素方法
        element: WebElement
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(3)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)
            raise e

    def find_ele_get_text(self, locator, value: str = None):
        # 获取元素text
        element: WebElement
        try:
            element_text = self._driver.find_element(*locator).text if isinstance(locator, tuple) else self._driver.find_element(locator, value).text
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element_text
        except Exception as e:
            self._driver.implicitly_wait(3)
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            for ele in self._black_list:
                ele_list = self._driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find_ele_get_text(locator, value)
            raise e

    def finds(self, locator):
        # 获取所有元素
        return self._driver.find_elements(*locator)

    def wait_for_ele_not_found(self, locator, value, time=5):
        # 定义显示等待方法
        WebDriverWait(self._driver, time).until_not(expected_conditions.text_to_be_present_in_element(locator, text_=value))

    def wait_for_ele_found(self, locator, time=5):
        # 显示等待
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    @staticmethod
    def get_data_with_yml(filename):
        # 从yml文件获取所有测试数据
        with open(current_path + "/data/" + filename + ".yml", "r", encoding="utf-8")as f:
            return yaml.safe_load(f)





