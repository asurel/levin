import sys

sys.path.append("..")


class Calc:

    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            return "输入类型错误"

    def sub(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        else:
            return "输入类型错误"

    def mul(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            return "输入类型错误"

    def div(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            try:
                return a / b
            except ZeroDivisionError:
                return "除数不能为0"
        else:
            return "输入类型错误"
