import pytest


@pytest.fixture()
def open_calc():
    print("打开计算器")
    from scripts.calc import Calc
    calc = Calc()
    yield calc
    print("关闭计算器")
