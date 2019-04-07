from common.commonDate import Common
from conftest import http
import pytest
import allure

@allure.feature('修改密码模块')
class Test_ChangePwd():
    @allure.story('修改密码成功')
    @pytest.mark.usefixtures("recoveryPwd")
    def test_changePwd_success(self):
        newPwd="123456789"
        data={'userId':"141",'userName':Common.userName,'oldPwd':Common.password,"password":newPwd}
        resp = http.post('/sys/changePwd',data)
        assert resp['code'] == 200
        assert resp['msg']=='操作成功'
        print("新密码修改成功")

@allure.story('改回密码成功')
@pytest.fixture()
def recoveryPwd():
    newPwd="123456"
    yield
    data={'userId':"141",'userName':Common.userName,'oldPwd':"123456789","password":newPwd}
    resp=http.post('/sys/changePwd', data)
    assert resp['code'] == 200
    assert resp['msg'] == '操作成功'
    print("旧密码改回成功")

