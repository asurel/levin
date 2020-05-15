#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/1514:30
# @Author:levin
# @File:test_action.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAction:

    def setup(self):
        # options = Options()
        # options.debugger_address = "127.0.0.1:9111"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_action(self):
        """鼠标单击、双击、右键"""
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("有道云笔记")
        ele_click = self.driver.find_element(By.XPATH, "//input[@value='click me']")
        ele_right_click = self.driver.find_element(By.XPATH, "//input[@value='right click me']")
        to_click = self.driver.find_element(By.XPATH, "//input[@value='dbl click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        time.sleep(3)
        action.double_click(ele_right_click)
        time.sleep(3)
        action.context_click(to_click)
        time.sleep(3)
        action.perform()

    @pytest.mark.skip
    def test_move_ele(self):
        """鼠标移动到固定位置ele"""
        self.driver.get("https://www.baidu.com/")
        time.sleep(3)
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        time.sleep(10)

    @pytest.mark.skip
    def test_drag_drop(self):
        """元素拖拽到固定位置drag_element→drop_element"""
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element).perform()
        # time.sleep(5)
        action.click_and_hold(drag_element).move_to_element(drop_element).perform()

    @pytest.mark.skip
    def test_keys(self):
        """模拟键盘输入,pause(1)表示延后一秒"""
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("name").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("pwd").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        time.sleep(5)

    def test_baidu(self):
        """滑动"""
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id("kw")
        elem = self.driver.find_element_by_id("su")
        el.send_keys("selenium")
        action = TouchActions(self.driver)
        action.tap(elem)
        action.perform()
        # 给定一个元素el，再给定一个坐标偏移量0代表横向不移动，2000代表纵向移动2000个像素位置
        action.scroll_from_element(el, 0, 2000).perform()
