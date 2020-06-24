#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/2614:26
# @Author:levin
# @File:test_add_member.py
import time

import allure
import pytest
import yaml

from app.page.app import App


# def get_data_info(key):
#     # 根据key获取对应的value数据
#     return BasePage().get_data_with_yml("add_member")[key]


class TestAddMember:

    def setup(self):
        # 启动app
        self.app = App()
        self.main = self.app.start().main()

    def teardown(self):
        # 关掉app
        self.app.stop()

    @pytest.mark.parametrize(("name", "phone", "email", "gender"), yaml.safe_load(open("./test_contact.yml", encoding="utf-8")))
    def test_add_member(self, name, phone, email, gender):
        # 测试添加成员
        self.invite_page = self.main.\
            to_address_list().\
            to_add_member().add_manually().add_name(name).\
            add_email(email).add_phone(phone).set_gender(gender).click_save()
        assert "成功" in self.invite_page.get_toast()

    @pytest.mark.parametrize("name", yaml.safe_load(open("./del_contact.yml", encoding="utf-8")))
    def test_del_member(self, name):
        # 测试删除成员
        self.edit_page = self.main.to_address_list().to_manage_contacts().to_edit_member(name).del_member()
        assert self.edit_page.get_member_name(name)
    # @pytest.mark.parametrize(("name", "gender", "phone", "email"), get_data_info("add"))
    # def test_add_member(self, name, gender, phone, email):
    #     # 测试添加成员
    #     self.invite_page = self.main.to_address_list().to_add_member().add_manually().add_name(name). \
    #         set_gender(gender).add_email(email).add_phone(phone).click_save()
    #     assert "成功" in self.invite_page.get_toast()

    # @pytest.mark.parametrize("name", get_data_info("del"))
    # def test_del_member(self, name):
    #     # 测试删除成员
    #     self.edit_page = self.main.to_address_list().to_manage_contacts().to_edit_member(name).del_member()
    #     assert self.edit_page.get_member_name(name) is True