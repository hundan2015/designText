# -*- coding:UTF-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def judge_title(seed:str, word: str):
    try:
        req = requests.get(url = seed)
        html = req.text
        div_bf = BeautifulSoup(html, features="html.parser")
        head = div_bf.find_all('title')
        for x in head:
            # print(x, word)
            if word in str(x):
                # print('YES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                return True
    except:
        return False
    return False


def getserver(s : str):
    dir = s.find('cn/')
    return s[:dir+3]
#返回
def geturl(seed : str, word : str):
    list = []
    server = getserver(seed)
    req = requests.get(url = seed)
    html = req.text
    div_bf = BeautifulSoup(html, features="html.parser")
    div = div_bf.find_all('a')
    for x in div:
        try:
            newurl = server + x.get('href')
        except:
            continue
        if(len(x.text) >= 4):
            print(x.text,newurl, sep = '|666|')
            if judge_title(newurl, word):
                list.append(newurl)

    print(div.__len__())
    return list

def getall_url(seed : str, word : str):
    list = []
    server = getserver(seed)
    list_tofind = []
    list_fed = []
    t = geturl(seed, word)
    list_tofind.append(seed)
    while list_tofind != None:
        try:
            print(list_tofind[0], '!!!!')
            a = geturl(list_tofind[0], word)
        except:
            break

        list_fed.append(list_tofind[0])
        for x in a:
            if t.count(x) == 0:
                print('!')
            if list_fed.count(x) == 0 and list_tofind.count(x) == 0:
                list_tofind.append(x)
                # print('append',x)
            if list.count(x) == 0:
                list.append(x)
                # print('append list', list.__len__())
                # print(list_tofind[0])
                # print(list_fed, list, list_tofind, sep='\n')
                # print(list.__len__(), list_tofind.__len__())
        # print(list_tofind)
        list_tofind.remove(list_tofind[0])
        print(list_tofind.__len__())
    return list
#
# server = 'http://cos.neu.edu.cn'
# target = 'http://cos.neu.edu.cn/1149/list.htm'
# keyword = '学院'
# # l = getall_url(target, keyword)
# l = geturl(target, keyword)
# print('function ended')
# for x in l:
#     print(x)
# # print(l.__len__())
