import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commonDate import Common
http=HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path="/sys/login"
    data={'userName':Common.userName,'password':Common.password}
    resp_login=http.post(path,data)
    Common.token = resp_login['object']['token']
    # resp_dict = json.loads(resp_login.text)
    # token = resp_dict["object"]["token"]
    assert resp_login["code"]==200
    print(resp_login)
    print("登录成功")

    # yield
    # headers['token']=token
    # resp= http.post(url="http://192.168.1.203:8083/sys/logout",
    #                  proxies=proxies,
    #                  data=None,
    #                  headers=headers)
    # assert resp.status_code==200
    # print("退出成功")