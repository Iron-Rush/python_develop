# RequestStudy.py
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)    # 请求状态码，200为成功
print('编码方式：{}'.format(r.encoding))
print('内容编码方式：{}'.format(r.apparent_encoding))
# 根据内容编码方式，设置encoding
r.encoding = 'utf-8'
print(type(r))          #r的状态类
print(r.headers)        #请求访问的头部信息
print(r.text)
# print(r.status_code)