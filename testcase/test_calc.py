import allure


class Calc:

    def add(self, a: int, b: int):
        return a + b

    def div(self, a, b):
        return a / b


class TestCalcAdd:
    calc = Calc()

    @allure.story("两个数都为正整数相加")
    def test_add_1(self):
        result = self.calc.add(1, 2)
        assert 3 == result

    @allure.story("两个数都为0相加")
    def test_add_2(self):
        result = self.calc.add(0, 0)
        assert 0 == result

    @allure.story("两个负数相加")
    def test_add_3(self):
        result = self.calc.add(-2, -3)
        assert -5 == result

    @allure.story("两个浮点数相加")
    def test_add_4(self):
        result = self.calc.add(5.4, 4.6)
        assert 10.0 == result

    @allure.story("整数和浮点数相加")
    def test_add_5(self):
        result = self.calc.add(7, 7.7)
        assert 14.7 == result


class TestCalcDiv:
    calc = Calc()

    @allure.story("两个数都为正整数")
    def test_div_1(self):
        result = self.calc.div(1, 2)
        assert 0.5 == result

    @allure.story("两个正整数相同")
    def test_div_2(self):
        result = self.calc.div(1, 1)
        assert 1 == result

    @allure.story("被除数为0")
    def test_div_3(self):
        result = self.calc.div(0, 1)
        assert 0 == result

    @allure.story("除数为0")
    def test_div_4(self):
        try:
            result = self.calc.div(0, 0)
        except ZeroDivisionError:
            print("除数不能为0")

    @allure.story("两个浮点数相除")
    def test_div_5(self):
        result = self.calc.div(1.5, 0.5)
        assert 3.0 == result

    @allure.story("两个负数相除")
    def test_div_6(self):
        result = self.calc.div(-3, -5)
        assert 0.6 == result

    @allure.story("一个负整数除以正整数")
    def test_div_7(self):
        result = self.calc.div(-3, 3)
        assert -1 == result
