import requests, urllib3
urllib3.disable_warnings()


class LoginUtils(object):
    def __init__(self, app_id, secret, code_id):
        self.url = "https://api.weixin.qq.com/sns/jscode2session"
        self.appid = app_id
        self.secret = secret
        self.jscode = code_id  # 前端传回的动态jscode

    def get_openid_and_sessionkey(self):
        # url一定要拼接，不可用传参方式
        # https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code
        url = self.url + "?appid=" + self.appid + "&secret=" + self.secret + "&js_code=" + self.jscode + "&grant_type=authorization_code"
        # 发送请求
        r = requests.get(url, timeout=3, verify=False)
        print(r.json())
        # 获取session_key
        session_key = r.json()['session_key']

        # 获取openid
        openid = r.json()['openid']
        return openid, session_key
