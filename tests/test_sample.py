import pytest

# 测试加法
def test_addition():
    assert 1 + 1 == 2

# 测试减法
def test_subtraction():
    assert 5 - 3 == 2

# 参数化测试加法
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (10, 5, 15)
])
def test_add_param(a, b, expected):
    assert a + b == expected

# 跳过的测试
@pytest.mark.skip(reason="暂时跳过")
def test_skip():
    assert 1 == 0

# 预期失败的测试
@pytest.mark.xfail(reason="已知bug,预期失败")
def test_xfail():
    assert 1 == 0