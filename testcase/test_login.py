from common.commonDate import Common
from conftest import http
class Test_Login():
    def test_login_success(self):
        data={"token":Common.token}
        resp=http.post("/sys/getUserInfo",data)
        assert resp["code"]==200