import pytest

@pytest.fixture()
def my_fixture():
    print("没钱")
    yield
    print("请下车")
class Test_class:
    @pytest.mark.debug
    def test_first(this):
        print("投币")
        # assert 1==2

    def test_sencond(this):
        print("投币")
        # assert 2==2
        # assert "h" in "haotest"

    @pytest.mark.debug
    @pytest.mark.usefixtures("my_fixture")
    def test_three(this):
        print("第三个测试用例")
    @pytest.mark.usefixtures("my_fixture")
    def test_four(this):
        print("第四个测试用例")
        assert 1 in [5,2,3]
    def test_five(this):
        print("第五个测试用例")
        assert 1 != 2

if __name__ == '__main__':
    pytest.main('-s')