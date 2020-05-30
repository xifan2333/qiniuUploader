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

    def set_current_bucket(self,i):
        self.current_bucket = self.buckets[i]

    def add_url(self, url):
        self.urls.append(url)

    def rm_url(self, url):
        self.buckets.remove(url)
    
    def set_current_url(self,i):
        self.current_url=self.urls[i]

    def set_config(self):
        self.config = {"ak": self.ak,
                       "sk": self.sk,
                       "buckets": self.buckets,
                       "current_bucket":self.current_bucket,
                       "urls":self.urls,
                       "current_url":self.current_url

                       }
        with open('./config.json', 'w') as f:
            json.dump(self.config, f)

