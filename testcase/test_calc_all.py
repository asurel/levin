import pytest
import sys
import allure

sys.path.append("..")


@allure.feature("测试计算器的加减乘除")
class TestCalcAll:

    @pytest.mark.add
    @pytest.mark.parametrize(("a", "b", "expect"),
                             [(1, 1, 2), (0, 0, 0), (-1, -1, -2), (0.1, 0.1, 0.2),
                              (1234567899999, 1234567899999, 2469135799998)])
    def calc_add(self, a, b, expect, open_calc):
        result = open_calc.add(a, b)
        assert expect == result

    @pytest.mark.sub
    @pytest.mark.parametrize(("a", "b", "expect"),
                             [(1, 1, 0), (0, 0, 0), (-1, -1, 0), (0.1, -0.2, 0.3),
                              (1234567899999, 1234567899998, 1)])
    def calc_sub(self, a, b, expect, open_calc):
        result = open_calc.sub(a, b)
        assert expect == result

    @pytest.mark.mul
    @pytest.mark.parametrize(("a", "b", "expect"),
                             [(1, 1, 1), (0, 0, 0), (-1, -1, 1), (0.1, 0.1, 0.11),
                              (1234567899999, 1234567899999, 1524157899707940864200001)])
    def calc_mul(self, a, b, expect, open_calc):
        result = open_calc.mul(a, b)
        assert expect == result

    @pytest.mark.div
    @pytest.mark.parametrize(("a", "b", "expect"),
                             [(1, 1, 1), (0, 0, "除数不能为0"), (-1, -1, 1), (0.1, 0.1, 1),
                              (1234567899999, 1234567899999, 1)])
    def calc_div(self, a, b, expect, open_calc):
        result = open_calc.div(a, b)
        assert expect == result
