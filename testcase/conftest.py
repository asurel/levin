import pytest
from scripts.calc import Calc


@pytest.fixture()
def open_calc():
    print("打开计算器")
    calc = Calc()
    yield calc
    print("关闭计算器")


def pytest_configure(config):
    marker_list = ["add", "sub", "mul", "div"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        if "_add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "_sub" in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif "_mul" in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif "_div" in item.nodeid:
            item.add_marker(pytest.mark.div)
