# RequestHead.py
import requests
r = requests.head('http://www.baidu.com')
print(r.headers)
print(r.text)
kv = {'key1' : 'value1', 'key2' : 'value2'}
r = requests.request('POST', 'http://python123.io/ws', data = kv)
print(r.request)