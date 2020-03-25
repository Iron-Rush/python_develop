# Demo4ClimbPicture.py
import requests
import os
# 定义根目录root
root = './/pics//'
url = 'https://images-cn.ssl-images-amazon.com/images/G/28/kindle/2017/Ruby/DPbannerresize/eanab_05._CB485978690_.jpg'
path = root + url.split('/')[-1]    # 以反斜杠分割的最后一部分为图片名
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f: #打开文件，并当作文件标识符f
            f.write(r.content)      #r.content表示响应内容的二进制格式，写入到f中
            f.close()
            print("文件保存成功")
    else:
        print('文件已存在')
except:
    print('爬取失败')
# r = requests.get(url)
# print(r.status_code)
# with open(path, 'wb') as f:
#     f.write(r.content)
# f.close()