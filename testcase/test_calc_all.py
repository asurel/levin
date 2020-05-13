import pytest
import sys
import allure
import yaml

sys.path.append("..")


def get_data_with_yml(filename):
    """从yml文件获取所有测试数据"""
    with open("./data/" + filename + ".yml", "r", encoding="utf-8")as f:
        return yaml.safe_load(f)


def get_data_info(key):
    """根据key获取对应的value数据"""
    return get_data_with_yml("calc_data")[key]


@allure.feature("测试计算器的加减乘除")
class TestCalcAll:

    @pytest.mark.parametrize(("a", "b", "expect"), get_data_info("add"))
    def calc_add(self, a, b, expect, open_calc):
        steps = get_data_with_yml("calc_steps")
        for step in steps:
            if step == "add":
                result = open_calc.add(a, b)
                assert expect == result

    @pytest.mark.parametrize(("a", "b", "expect"), get_data_info("sub"))
    def calc_sub(self, a, b, expect, open_calc):
        result = open_calc.sub(a, b)
        assert expect == result

    @pytest.mark.parametrize(("a", "b", "expect"), get_data_info("mul"))
    def calc_mul(self, a, b, expect, open_calc):
        result = open_calc.mul(a, b)
        assert expect == result

    @pytest.mark.parametrize(("a", "b", "expect"), get_data_info("div"))
    def calc_div(self, a, b, expect, open_calc):
        steps = get_data_with_yml("calc_steps")
        for step in steps:
            if step == "div":
                result = open_calc.div(a, b)
                assert expect == result
