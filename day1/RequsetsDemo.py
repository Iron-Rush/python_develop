# RequsetsDemo.py
import requests
def getURL(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()            # 如果访问发生异常，则抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return '产生异常'
if __name__ == '__main__':
    url = 'https://www.baidu.com'
    print(getURL(url))