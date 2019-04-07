import requests
import json
# proxies={"http":"http://localhost:8888"}
# headers={}
# headers["Content-Type"]="application/json;charset=UTF-8"
# http=requests.session()
# resp=http.post(url="http://192.168.1.203:8083/sys/login",
#                    proxies=proxies,
#                    data='{"userName":"18210034706","password":"123456"}',
#                    headers=headers)
#
# resp_dict=json.loads(resp.text)
# token=resp_dict["object"]["token"]
# headers['token']=token
# resp=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                    proxies=proxies,
#                    data=token,
#                    headers=headers)
# print(resp.text)
# print(resp.headers)
# print(resp.url)
# print(resp.cookies)
# print(resp.encoding)
# print(resp.status_code)
from common.commonDate import Common
class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={"Content-Type":"application/json;charset=UTF-8"}
    def post(self,path,data):
        proxies=Common.proxies
        host=Common.host
        data_json=json.dumps(data)
        if Common.token is not None:
            self.headers['token']=Common.token
        resp_login = self.http.post(url=host+path,
                                    proxies=proxies,
                                    data=data_json,
                                    headers=self.headers)
        assert resp_login.status_code==200
        resp_json=resp_login.text
        resp_dict=json.loads(resp_json)
        return  resp_dict
