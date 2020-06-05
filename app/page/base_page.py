#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/259:05
# @Author:levin
# @File:base_page.py
import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os

from app.page.wrapper import handle_black

current_path = os.path.abspath(os.path.dirname(__file__)).split('\\app')[0]


class BasePage:
    _params ={}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly_wait(self, time):
        # 设置隐式等待
        self._driver.implicitly_wait(time)

    @handle_black
    def find(self, locator, value: str = None):
        # 定位元素方法
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def find_ele_get_text(self, locator, value: str = None):
        # 获取元素text
        if isinstance(locator, tuple):
            text = self._driver.find_element(*locator).text
        else:
            text = self._driver.find_element(locator, value).text
        return text

    @handle_black
    def finds(self, locator, value: str = None):
        # 获取所有元素
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def wait_for_ele_not_found(self, locator, value, time=5):
        # 定义显示等待方法
        WebDriverWait(self._driver, time).until_not(expected_conditions.text_to_be_present_in_element(locator, text_=value))

    def wait_for_ele_found(self, locator, time=5):
        # 显示等待
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))

    # @staticmethod
    # def get_data_with_yml(filename):
    #     # 从yml文件获取所有测试数据
    #     tmp_path = current_path.replace("\\", "/")
    #     expect_path = tmp_path + "/data/" + filename + ".yml"
    #     print(expect_path)
    #     with open(expect_path, "r", encoding="utf-8")as f:
    #         return yaml.safe_load(f)

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        # 转为json字符串
        raw = json.dumps(steps)
        for key, value in self._params.items():
            # 获取函数名并把json串中对应的key替换为value
            raw = raw.replace('${' + key + '}', value)
        # 再把json串转为python对象
        steps = json.loads(raw)
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if "len>0" == action:
                    elements = self.finds(step["by"], step["locator"])
                    return len(elements) > 0





