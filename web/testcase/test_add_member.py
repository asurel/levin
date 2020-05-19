#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/1915:39
# @Author:levin
# @File:test_add_member.py
from web.page.main import MainPage


class TestAddMember:
    def setup(self):
        self.main_page = MainPage()

    def test_add_member(self):
        """测试添加成员"""
        add_member = self.main_page.to_add_member()
        add_member.add_member()
        assert add_member.get_member_name("a123456")