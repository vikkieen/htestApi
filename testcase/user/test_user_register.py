from common.commonDate import Common
import random
from conftest import http
from testcase.user.test_user_loadUserList import Test_LoadUserList
import allure

@allure.feature('修改密码模块')
class Test_Register():
    nickname = str(random.randint(10000000, 100000000))
    userName = '135' + nickname

    @allure.story('注册成功')
    def test_register_success(self):

        print(self.userName)
        data={"nickName":"whoami","userName":self.userName,"telNo":"","email":"","address":"","roleIds":"","regionId":1,"regionLevel":1}
        resp = http.post('/user/saveOrUpdateUser',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        print("注册用户成功")

    @allure.story('登录成功')
    def test_login(self):
        print(self.userName)
        data={'userName':self.userName,'password':Common.password}
        resp=http.post('/sys/login',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print("登录成功")
        self.userId=resp['object']['userId']
        print('******',self.userId)

    @allure.story('比较成功')
    def test_compare(self):
        loadUserList = Test_LoadUserList()
        userId=loadUserList.test_loadUserList_success()
        print('----------',userId)
        print('----/***', self.test_login().userId)
        assert userId==self.userId
        print("yes")
