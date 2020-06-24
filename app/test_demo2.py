#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/2011:17
# @Author:levin
# @File:test_demo2.py
import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDemo2:

    def setup(self):
        desired_caps = {}
        # com.xueqiu.android/.view.WelcomeActivityAlias
        desired_caps["platformName"] = "Android"
        # desired_caps["platformVersion"] = "8.0.0"
        # desired_caps["deviceName"] = "emulator-5554"
        desired_caps["appPackage"] = "com.xueqiu.android"
        desired_caps["appActivity"] = ".view.WelcomeActivityAlias"
        desired_caps["udid"] = os.getenv("udid", None)
        desired_caps["noReset"] = True
        # desired_caps["skipDeviceInitialization"] = True
        desired_caps["unicodeKeyBoard"] = True
        desired_caps["resetKeyBoard"] = True
        self.driver = webdriver.Remote("http://192.168.2.152:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("current_price").text)
        assert current_price > 200

    def test_touch(self):
        action = TouchAction(self.driver)
        action.press(x=731, y=2083).wait(300).move_to(x=731, y=400).release().perform()

    def test_hk(self):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        current_price = float(self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        assert current_price > 200

    def test_login(self):
        # 注意写法：定位元素必须要写双引号，所以外面就用单引号，不然会报错,也可组合定位，直接在后面接着写元素属性和值就行
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的").resourceId("com.xueqiu.android:id/tab_name")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("登录雪球")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号或邮箱")').send_keys("12345678901")
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("请输入登录密码")').send_keys("123456")
        self.driver.find_element_by_id("com.xueqiu.android:id/button_next").click()
        # login_text = self.driver.find_element_by_id("com.xueqiu.android:id/md_content").text
        # com.xueqiu.android:id/md_buttonDefaultPositive
        self.driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultPositive").click()
        time.sleep(3)
        # assert login_text == "用户名或密码错误"
