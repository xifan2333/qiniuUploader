from qiniu import Auth, put_file
#需要填写你的 Access Key 和 Secret Key
access_key = '-FrVRtN6n86rbnw6iwLF8SZHHJ8mv2NNJNtNYYIL'
secret_key = '6XraLGydOPzTtG3Yrs65e4VKPu2X7M-oXUg7PvDu'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'image'
#上传后保存的文件名
key = 'my-python-logo.png'
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
localfile = './2.jpg'
ret, info = put_file(token, key, localfile)
print(info)


# class QiNiu:
#     def __init__():
