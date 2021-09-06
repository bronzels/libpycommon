import requests


class WXAccessTokenUtils:
    def __init__(self, app_id, secret):
        self.grant_type = "client_credential"
        self.app_id = app_id
        self.secret = secret

    def url(self):
        return "https://api.weixin.qq.com/cgi-bin/token?grant_type={}&appid={}&secret={}".format(
            self.grant_type, self.app_id, self.secret)

    def get_access_code(self):
        response = requests.get(url=self.url())
        response = response.json()
        print(response["access_token"])
        if "access_token" in response:
            return response["access_token"]
        else:
            return "500"


class WXQRCodeUtils:
    def __init__(self, access_token, path, width):
        self.access_token = access_token
        self.path = path
        self.width = width

    def url(self):
        return "https://api.weixin.qq.com/cgi-bin/wxaapp/createwxaqrcode?access_token={}".format(self.access_token)

    def json_formatter(self):
        json = {
            "path": self.path,
            "width": self.width
        }
        return json

    def get_qr_code(self):
        response = requests.post(url=self.url(), json=self.json_formatter())
        return response.content
