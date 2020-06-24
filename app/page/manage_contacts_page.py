#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/2710:25
# @Author:levin
# @File:manage_contacts_page.py
from selenium.webdriver.common.by import By
from app.page.base_page import BasePage
from app.page.edit_member_page import EditMemberPage


class ManageContactsPage(BasePage):

    def to_edit_member(self, name):
        # 进入编辑成员页面
        # edit_name_ele = f'//*[@text="{name}"]/../../../..//*[@resource-id="com.tencent.wework:id/fdh"]'
        # self.find(By.XPATH, edit_name_ele).click()
        self._params["name"] = name
        self.steps("../page/manage_contacts.yml")
        return EditMemberPage(self._driver)

    def get_member_name(self, name):
        # 获取成员姓名
        self._params["name"] = name
        get_name_ele = f'//*[@text="{name}"]'
        self.wait_for_ele_not_found((By.XPATH, get_name_ele), time=3, value=name)
        return self.steps("../page/manage_contacts.yml")
        # member_name = self.finds((By.XPATH, get_name_ele))
        # if len(member_name) < 1:
        #     return True
        # else:
        #     return False