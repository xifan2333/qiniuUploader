from qiniu import Auth, put_file
import os
import time
import json


class QiNiu():
    def __init__(self, ak, sk, buckets, urls):
        self.ak = ak
        self.sk = sk
        self.buckets = buckets
        self.urls = urls
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




