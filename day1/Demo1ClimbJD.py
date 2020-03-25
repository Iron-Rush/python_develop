# Demo1ClimbJD.py
import requests
# r = requests.get('https://item.jd.com/34527235241.html')
# print("访问链接状态：{}".format(r.status_code))
# print("页面编码：{}".format(r.encoding))     #http头部分解析出编码为gbk
# print(r.text)

url = 'https://item.jd.com/34527235241.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(r.encoding)
    print(r.text[:1000])
except:
    print('爬取失败')