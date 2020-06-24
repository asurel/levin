#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/259:05
# @Author:levin
# @File:app.py
import os

from appium import webdriver
from app.page.base_page import BasePage
from app.page.main_page import MainPage


class App(BasePage):

    def start(self):
        # 判断driver，初始化driver
        if self._driver is None:
            desired_caps = {}
            # com.tencent.wework/com.tencent.wework.launch.WwMainActivity
            desired_caps["platformName"] = "Android"
            desired_caps["platformVersion"] = "6.0.1"
            desired_caps["deviceName"] = "127.0.0.1:7555"
            # desired_caps["udid"] = os.getenv("udid",None)
            desired_caps["appPackage"] = "com.tencent.wework"
            desired_caps["appActivity"] = "com.tencent.wework.launch.WwMainActivity"
            desired_caps["noReset"] = True
            desired_caps["skipDeviceInitialization"] = True
            desired_caps["unicodeKeyBoard"] = True
            desired_caps["resetKeyBoard"] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            # self._driver = webdriver.Remote("http://192.168.2.148:4723/wd/hub", desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(3)
        return self

    def stop(self):
        self._driver.quit()

    def main(self):
        # 跳转至主页面
        return MainPage(self._driver)