#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/1914:50
# @Author:levin
# @File:add_member_page.py
from selenium.webdriver.common.by import By

from web.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        # 添加成员
        self.find(By.ID, "username").send_keys("a123456")
        self.find(By.ID, "memberAdd_english_name").send_keys("第一次添加的用户")
        self.find(By.ID, "memberAdd_acctid").send_keys("abde")
        self.find(By.XPATH, "//*[@name='gender' and @value='2']").click()
        self.find(By.ID, "memberAdd_phone").send_keys("12345678901")
        self.find(By.ID, "memberAdd_telephone").send_keys("028-12457896")
        self.find(By.ID, "memberAdd_mail").send_keys("123@qq.com")
        self.find(By.ID, "memberEdit_address").send_keys("成都市高新区楚峰国际")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

    def update_page(self):
        content: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
        return [int(x) for x in content.split('/', 1)]

    def get_member_name(self, value):
        self.wait_tobe_click((By.CSS_SELECTOR, ".ww_checkbox"))
        if len(self.finds(By.CSS_SELECTOR, ".ww_pageNav_info_text")) >= 1:
            cur_page, total_page = self.update_page()
            while True:
                elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
                for element in elements:
                    if value == element.get_attribute("title"):
                        return True
                cur_page = self.update_page()[0]
                if cur_page == total_page:
                    return False
                self.find(By.CSS_SELECTOR, '.js_next_page').click()
        else:
            all_name = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for name in all_name:
                if value == name.get_attribute("title"):
                    return True