#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/6/817:17
# @Author:levin
# @File:conftest.py
import os
import shlex
import signal
import subprocess
import time

import allure
import pytest


@pytest.fixture(scope="class", autouse=True)
def record():
    cmd = shlex.split("scrcpy --record tmp.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    # os.kill(p.pid, signal.CTRL_C_EVENT)
    os.popen('taskkill.exe /pid:' + str(p.pid))
    time.sleep(1)
    with open("tmp.mp4", "rb") as f:
        video_file = f.read()
    allure.attach(video_file, name="测试用例视频", attachment_type=allure.attachment_type.MP4)
