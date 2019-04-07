from common.commonDate import Common
from conftest import http

class Test_LoadUserList:
    def test_loadUserList_success(self):
        data={"pageCurrent":1,"pageSize":10,"nickName":"","userName":"","regionId":1}
        resp = http.post('/user/loadUserList',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        print("查看列表成功")
        return resp["object"]["list"][0]["id"]
