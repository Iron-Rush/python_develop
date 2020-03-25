# Demo3ClimbSearchEngine.py
# 提交关键词至搜索引擎
# 百度关键词接口：http://wwww.baidu.com/s?wd=keyword
# 360关键词接口： http://www.so.com/s?q=keyword
import requests
try:
    head = {'user-agent': 'Mozilla/5.0'}
    keyWord2 = {'q': 'Python'}
    r2 = requests.get('http://www.so.com/s', params=keyWord2, headers=head)
    r2.encoding = r2.status_code
    r2.raise_for_status()
    print(r2.status_code)
    print(r2.request.url)
    print(len(r2.text))
except:
    print('爬取失败')

# keyWord = {'wd': 'Python'}
# r = requests.get('http://www.baidu.com/s', params=keyWord, headers=head)
# r.encoding = r.status_code
# print(r.status_code)
# print(r.request.url)    # 百度爬虫已设安全认证