#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/2514:08
# @Author:levin
# @File:address_page.py
from selenium.webdriver.common.by import By

from app.page.base_page import BasePage
from app.page.manage_contacts_page import ManageContactsPage
from app.page.member_invite_page import MemberInvite


class AddressPage(BasePage):
    def to_add_member(self):
        # 添加成员
        # self.find((By.XPATH, "//*[@text='添加成员']")).click()
        self.steps("../page/addresspage.yml")
        return MemberInvite(self._driver)

    def to_manage_contacts(self):
        # 跳转至管理联系人页面
        # self.find(By.ID, "gvi").click()
        self.steps("../page/addresspage.yml")
        return ManageContactsPage(self._driver)