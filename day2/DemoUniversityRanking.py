# DemoUniversityRanking.py
# http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html
# 输出大学排名信息(排名，大学名称，总分)
import requests
import bs4
from bs4 import BeautifulSoup
# 从网络上获取大学排名网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)   #获取页面
        r.raise_for_status()                #判断是否产生异常
        r.encoding = r.apparent_encoding    #修改编码
        return r.text                       #返回网页信息内容
    except:
        return "error"                      #若产生异常返回error

# 提取网页内容中信息到合适的数据结构
def fillUnivList(ulist, html):
    # 利用bf库煲汤
    soup = BeautifulSoup(html, "html.parser")
    '''tbody中，每个tr标签代表一个大学的数据信息
    tr标签每个td标签代表一个属性
    提取需要的信息，保存至uinfo中'''
    # 查找html中的tbody标签，遍历它的孩子
    for tr in soup.find('tbody').children:
        # 判断这个子类是否是标签类型
        if isinstance(tr, bs4.element.Tag):
            # 查询tr标签中的全部td标签
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

# 利用数据结构展示并输出结果
def printUnivList(ulist, num):
    # print("{:^10}\t{:^10}\t{:^10}".format("排名", "学校名称", "总分"))
    # 优化输出，制作输出模版tplt
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        # print("{0:^10}\t{1:^10}\t{2:^10}".format(u[0], u[1], u[2]))
        # 优化输出，利用tplt模版，和chr(12288)中文占位符
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    # printUnivList("Suc" + str(num))

def main():
    uinfo = []      #将大学信息放到列表uinfo中
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)         #根据url链接获取HTML
    if html == "error":             #判断提取过程是否出错
        print(html)
    else:
        fillUnivList(uinfo, html)   #将HTML信息提取后放到uinfo中
        printUnivList(uinfo, 40)    #列出前20的大学信息
main()
