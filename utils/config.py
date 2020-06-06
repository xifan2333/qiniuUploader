import json


class Config():
    @staticmethod
    def get_config():
        with open('./config.json', 'r',encoding='utf-8') as f:
            confing = json.load(f)
            return confing

    def __init__(self, ak="", sk="",buckets=[],urls=[],current_bucket='',current_url=''):
        self.ak = ak
        self.sk = sk
        self.buckets = buckets
        self.urls = urls
        self.current_bucket = current_bucket
        self.current_url = current_url

    def add_buket(self, bucket):
        self.buckets.append(bucket)

    def rm_bucket(self, bucket):
        self.buckets.remove(bucket)


    def add_url(self, url):
        self.urls.append(url)

    def rm_url(self, url):
        self.urls.remove(url)

    def set_config(self,ak="",sk="",bucket="",url=""):
        self.config = {"ak": ak or self.ak,
                       "sk": sk or self.sk,
                       "buckets": self.buckets,
                       "current_bucket":bucket or self.current_bucket,
                       "urls":self.urls,
                       "current_url":url or self.current_url

                       }
        with open('./config.json', 'w') as f:
            json.dump(self.config, f)

