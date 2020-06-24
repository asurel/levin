#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/2514:10
# @Author:levin
# @File:member_invite_page.py
from selenium.webdriver.common.by import By
from app.page.base_page import BasePage


class MemberInvite(BasePage):

    def add_manually(self):
        # 手动添加方法
        from app.page.add_contact_page import AddContact
        # self.find(By.XPATH, "//*[@text='手动输入添加']").click()
        # self.steps("../page/member_invite.yml")
        return AddContact(self._driver)

    def get_toast(self):
        # 获取当前页面的toast
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text