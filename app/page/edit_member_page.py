#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/2710:31
# @Author:levin
# @File:edit_member_page.py
from appium.webdriver.common.mobileby import MobileBy
from app.page.base_page import BasePage


class EditMemberPage(BasePage):

    def del_member(self):
        # 删除成员
        from app.page.manage_contacts_page import ManageContactsPage
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0))').click()
        self.find(MobileBy.ID, "b_a").click()
        return ManageContactsPage(self._driver)