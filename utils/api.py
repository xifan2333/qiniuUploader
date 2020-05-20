from qiniu import Auth, put_file
import os
import time
import json


class QiNiu():
    def __init__(self, ak, sk, bucket, url):
        self.ak = ak
        self.sk = sk
        self.bucket = bucket
        self.url = url
    def auth(self):
        self.q = Auth(self.ak, self.sk)
        return self

    def set_path(self, path):
        self.path = path
        self.key = f'{int(time.time())}{os.path.basename(path)}'
        return self

    def get_token(self):
        self.token = self.q.upload_token(self.bucket, self.key, 3600)
        return self

    def upload(self):
        info = put_file(self.token, self.key, self.path)[1]
        return  f'{self.url}{json.loads(info.text_body)["key"]}' if info.status_code==200 else info.exception

ak = "-FrVRtN6n86rbnw6iwLF8SZHHJ8mv2NNJNtNYYIL"
sk = "6XraLGydOPzTtG3Yrs65e4VKPu2X7M-oXUg7PvDu"
bucket="image"
url = "http://images.xifan.fun/"



