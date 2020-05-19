#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/1914:42
# @Author:levin
# @File:main.py
from selenium.webdriver.common.by import By

from web.page.add_member_page import AddMember
from web.page.base_page import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def to_add_member(self):
        self.find(By.ID, "menu_contacts").click()
        self.wait_tobe_click((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)"))
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        return AddMember(self._driver)