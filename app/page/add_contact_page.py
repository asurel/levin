#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/2613:59
# @Author:levin
# @File:add_contact_page.py
from selenium.webdriver.common.by import By
from app.page.base_page import BasePage


class AddContact(BasePage):

    def add_name(self, name):
        # 添加姓名
        # self.find(By.XPATH, "//*[@text='姓名　']/..//*[@resource-id='com.tencent.wework:id/au7']").send_keys(name)
        self._params["name"] = name
        self.steps("../page/add_contact.yml")
        return self

    def set_gender(self, gender="男"):
        # 选择性别
        # self.find(By.XPATH, "//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/dvl']").click()
        # gender_ele = f'//*[@text="{gender}"]'
        # self.wait_for_ele_found((By.XPATH, gender_ele))
        # self.find(By.XPATH, gender_ele).click()
        self._params["gender"] = gender
        self.steps("../page/add_contact.yml")
        return self

    def add_phone(self, phone):
        # 添加手机号
        self._params["phone"] = phone
        self.steps("../page/add_contact.yml")
        # self.find(By.XPATH, "//*[@text='手机　']/..//*[@resource-id='com.tencent.wework:id/eqx']").send_keys(phone)
        return self

    def add_email(self, email):
        # 添加邮箱
        # self.find(By.XPATH, "//*[@text='邮箱　']/..//*[@resource-id='com.tencent.wework:id/au7']").send_keys(email)
        self._params["email"] = email
        self.steps("../page/add_contact.yml")
        return self

    def click_save(self):
        # 点击保存
        # self.find(By.ID, "com.tencent.wework:id/gvk").click()
        self.steps("../page/add_contact.yml")
        from app.page.member_invite_page import MemberInvite
        return MemberInvite(self._driver)