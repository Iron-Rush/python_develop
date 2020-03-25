# Demo2ClimbAmazon.py
import requests
url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
# r = requests.get(url)
# r.encoding = r.apparent_encoding
# print('访问状态码{}'.format(r.status_code))  #状态码503，访问不正确
# # print(r.text)
# print(r.request.headers)
# # {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# kv = {'user-agent': 'Mozilla/5.0'}  #Mozilla5.0，标准浏览器标识字段
# r2 = requests.get(url, headers=kv)
# print('更改标识后的访问状态码：{}'.format(r2.status_code))  #状态码变回200，真正获得到页面
# print(r2.request.headers)
# # {'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# print(r2.text[:1000])
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)   #模拟浏览器向服务器提供http请求
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败')
