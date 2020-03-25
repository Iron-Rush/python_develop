# Demo5ClimbIPSearch.py
import requests
# http://m.ip138.com/ip.asp?ip=ipaddress params=keyWord2
head = {'user-agent': 'Mozilla/5.0'}
keyWord = {'ip': '101.38.26.189'}
url = "http://m.ip138.com/ip.asp"
try:
    r = requests.get(url, params=keyWord, headers=head)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('爬取失败')
# r = requests.get(url + '101.38.26.189' + '&action=2')
# url = 'https://www.ip138.com/iplookup.asp?ip=101.38.26.189&action=2'
# r = requests.get(url)
# print(r.status_code)