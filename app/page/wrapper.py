#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/6/216:49
# @Author:levin
# @File:wrapper.py
import logging
import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    # 异常处理
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        from app.page.base_page import BasePage
        _black_list = [(By.XPATH, "//*[@text='手动输入添加']"),
                       (By.ID, "image_cancel"),
                       (By.XPATH, "//*[@text='下次再说']"),
                       (By.XPATH, "//*[@text='跳过']"),
                       (By.XPATH, "//*[@text='确定']")
                       ]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]
        try:
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            instance.set_implicitly_wait(10)
            return element
        except Exception as e:
            instance.save_screen("error_img.png")
            with open("error_img.png", "rb") as f:
                content = f.read()
            allure.attach(content, name="未找到元素截图", attachment_type=allure.attachment_type.PNG)
            logging.error("element not found, handle black list")
            instance.set_implicitly_wait(3)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                ele_list = instance.finds(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper
