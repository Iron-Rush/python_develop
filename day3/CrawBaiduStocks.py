# CrawBaiduStocks.py
import requests
from bs4 import BeautifulSoup
import traceback
import re


# 获取页面信息,默认设置编码为utf-8
def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 爬取固定网页/网站时，可不获取apparent_enconding,直接赋值即可
        r.encoding = code
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 获取股票信息列表(存储股票信息的列表，和获取股票列表的URL)
# <li><a target="_blank" href="http://quote.eastmoney.com/sh500001.html">基金金泰(500001)</a></li>
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    # 找到全部a标签，并遍历进行处理
    a = soup.find_all('a')
    for i in a:
        try:
            # 获取a标签中的全部超链接至href
            href = i.attrs['href']
            # 以s开头，中间是h或z，后面跟着六位数字(sh/sz500001)
            # 符合条件的文本，追加到lst中
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


# 获取每只个股的信息并存至指定路径(股票信息列表，获取股票详情的URL，存储股票信息的路径)
def getStockInfo(lst, stockURL, fpath):
    # 遍历列表中每条股票编码
    for stock in lst:
        # 生成该股票对应的url，并获取页面
        url = stockURL + stock + ".html"
        html = getHTMLText(url, 'GB2312')
        # html = getHTMLText(url)
        try:
            # 判断页面是否为空
            if html == '':
                continue
            # 生成字典，记录页面提取的股票信息
            infoDict = {}
            soup = BeautifulSoup(html, "html.parser")
            # 获取股票所在的div标签
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            # 获取股票名称，以键值对的形式存储至字典中
            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
            # 找到股票信息中，全部键的部分，存储至keyList
            keyList = stockInfo.find_all('dt')
            # 找到股票信息中，全部值的部分，存储至valueList
            valueList = stockInfo.find_all('dd')
            # 利用for循环，将keyList和valueList合并至字典中
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            # 将字典追写至目标文件中
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            # 详细的错误信息
            traceback.print_exc()
            continue


def main():
    # 获取股票列表的链接
    stock_list_url = 'https://quote.eastmoney.com/stocklist.html'
    # 获取股票详情的链接
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    # 输出文件路径
    output_file = './stockInfo.txt'
    # output_file = 'D:/BaiduStockInfo.txt'
    # 定义列表，用于存储股票信息
    slist = []
    # 获取股票列表
    getStockList(slist, stock_list_url)
    # 根据股票列表，获取股票详细信息并存储到文件中
    getStockInfo(slist, stock_info_url, output_file)


# 调用main，启动函数
main()
