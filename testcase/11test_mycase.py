import pytest
@pytest.fixture()
def my_fixture():
    print("初始化操作")
@pytest.mark.usefixtures("my_fixture")
def test_first():
    print("第一个测试用例")
    assert 1==2
@pytest.mark.debug
@pytest.mark.usefixtures("my_fixture")
def test_sencond():
    print("第二个测试用例")
    assert 2==2
    assert "h" in "haotest"
@pytest.mark.usefixtures("my_fixture")
def test_three():
    print("第三个测试用例")
@pytest.mark.usefixtures("my_fixture")
def test_four():
    print("第四个测试用例")
    assert 1 in [5,2,3]
@pytest.mark.usefixtures("my_fixture")
def test_five():
    print("第五个测试用例")
    assert 1 != 2

if __name__ == '__main__':
    pytest.main('-s')