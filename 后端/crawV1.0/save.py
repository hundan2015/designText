#爬取网址
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
html = urlopen('http://cos.neu.edu.cn/2019/0716/c1129a137941/page.htm')
obj = bf(html.read(),'html.parser')
title = obj.span
print(title)
'''

#获取子页面网址
'''
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     server = 'http://cos.neu.edu.cn/'
     target = 'http://cos.neu.edu.cn/1156/list.htm'
     req = requests.get(url = target)
     html = req.text
     div_bf = BeautifulSoup(html, features="html.parser")
     div = div_bf.find_all('div', class_ = 'news_content')
     # print(div[0])
     a_bf = BeautifulSoup(str(div[0]))
     a = a_bf.find_all('a')
     for each in a:
          print(each.string,server + each.get('href'))
'''

#获取text文本
'''# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     server = 'http://cos.neu.edu.cn/'
     target = 'http://cos.neu.edu.cn/2021/0611/c1156a198646/page.htm'
     req = requests.get(url = target)
     html = req.text
     div_bf = BeautifulSoup(html, features="html.parser")
     print(div_bf.text)'''



#获取网址半成品
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def geturl(seed : str, word : str):
    list = []

    req = requests.get(url = target)
    html = req.text
    div_bf = BeautifulSoup(html, features="html.parser")
    # div = div_bf.find_all('div', class_ = 'news_content')
    # div = div_bf.find_all('ul', class_ = 'lis')
    div = div_bf.find_all('a')
    for x in div:
        print(x.text,server + x.get('href'), sep = '[666]')
    return 0
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
        try:
            newurl = server + each.get('href')
            html_in = urlopen(newurl)
            tem_bf1 = BeautifulSoup(html_in, features="html.parser")
            t_title = tem_bf1.find_all('title')
            if(tem_bf1.head.title != 0):
                for t_titles_son in t_title:
                    if(t_titles_son.text != None):
                        print(t_titles_son.text)
                print(newurl)
        except:
            pass

    # obj = bf(html.read(),'html.parser')
    # title = obj.span
    # print(title)
    # return list


server = 'http://cos.neu.edu.cn/'
target = 'http://cos.neu.edu.cn/1156/list.htm'
# server = 'http://sba.neu.edu.cn/'
# target = 'http://sba.neu.edu.cn/868/list.htm'
keyword = '夏令营'
geturl(target, keyword)
'''
