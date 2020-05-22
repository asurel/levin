#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/229:59
# @Author:levin
# @File:test_search.py
from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import TouchActions
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:

    def setup(self):
        desired_caps = {}
        # com.xueqiu.android/.view.WelcomeActivityAlias
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "8.0.0"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["noReset"] = True
        # skipDeviceInitialization跳过appium初始化的一些安装，提升运行速度
        desired_caps["skipDeviceInitialization"] = True
        desired_caps["unicodeKeyBoard"] = True
        desired_caps["resetKeyBoard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("content", ["阿里巴巴", "京东", "新浪"])
    def test_search(self, content):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys(content)
        self.driver.find_element_by_xpath(f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{content}']").click()
        content_by = f"//*[@text='{content}']/../..//*[@resource-id='com.xueqiu.android:id/follow_btn']"
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, content_by)))
        self.driver.find_element(By.XPATH, content_by).click()
        time.sleep(4)
        bbs = self.driver.find_element(By.XPATH, f"//*[@text='{content}']/../..//*[@resource-id='com.xueqiu.android:id/followed_btn']").text
        assert bbs == "已添加"


