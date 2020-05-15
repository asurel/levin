#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/149:50
# @Author:levin
# @File:demo.py
import shelve

import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class TestDemo:
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9111"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_company_chat(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cookies")
        # db["cookie"] = self.driver.get_cookies()
        cookies = db["cookie"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_css_selector("#menu_contacts").click()
        time.sleep(3)
        db.close()


if __name__ == '__main__':
    pytest.main()
