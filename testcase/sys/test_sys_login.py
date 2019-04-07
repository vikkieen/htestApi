from common.commonDate import Common
from conftest import http

class Test_Login():

    def test_login_success(self):
        data={'userName':Common.userName,'password':Common.password}
        resp=http.post('/sys/login',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        assert resp['object']['userId']==141

    def test_login_fail(self):
        data={
            'userName':Common.userName,
            'password':"12345678"
        }
        resp=http.post('/sys/login',data)
        assert resp['code']==410
        assert resp['msg']=='用户名或密码错误'

    def test_login_fail2(self):
        data = {
            'userName':"13010203041",
            'password':Common.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code']==301
        assert resp['msg']=='用户不存在'
    def test_login_fail3(self):
        data = {
            'userName':"130102030401314",
            'password':Common.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code']==301
        assert resp['msg']=='用户不存在'
    def test_login_fail4(self):
        data = {
            'userName':"",
            'password':Common.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code']==3010
        assert resp['msg']=='此账户禁止登录'
    def test_login_fail5(self):
        data = {
            'userName':Common.password,
            'password':""
        }
        resp = http.post('/sys/login', data)
        assert resp['code']==301
        assert resp['msg']=='用户不存在'