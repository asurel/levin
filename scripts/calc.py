import sys
sys.path.append("..")


class Calc:

    def add(self, a: int, b: int):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "除数不能为0"


