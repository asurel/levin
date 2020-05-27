#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/259:27
# @Author:levin
# @File:main_page.py
from selenium.webdriver.common.by import By

from app.page.address_page import AddressPage
from app.page.base_page import BasePage


class MainPage(BasePage):

    def to_address_list(self):
        # 跳转至联系人页面
        self.find((By.XPATH, "//*[@text='通讯录']")).click()
        return AddressPage(self._driver)