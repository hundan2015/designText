# -*- coding:UTF-8 -*-
from urllib.request import urlopen
import time
start_time = time.perf_counter()
from bs4 import BeautifulSoup
import requests
from getpage import geturl
from getpage import tools

print('import所用时间',time.perf_counter() - start_time)
keyword = '硕士'

#读入搜索资源网站
print('start main function!')
source_seed = []
with open("search.txt", "r", encoding="utf-8") as in_txt:
    while True:
        try:
            source_seed.extend(eval(in_txt.readline()))
        except:
            break
print('import root website ended')
#主程序
sites = []
dir = 0
start_time = time.perf_counter()
for webs in source_seed:
    sites.extend(geturl.geturl(webs, keyword))
    dir+=1
    print('{} seed website searched'.format(dir))
#获得目标网站 在site列表里
#计时器
print('爬取网址所用时间',time.perf_counter() - start_time)

#生成网页数据
list_data = []
#TITLE:标题 HREF:网址 CONTEXT:内容div
for target in sites:
    req = requests.get(url = target)
    html = req.text
    div_bf = BeautifulSoup(html, features="html.parser")
    head = div_bf.find('title')
    print(head.text, target)
    list_data.append({
        'TITLE':head.text,
        'HREF':target,
        'CONTEXT':tools.get_word(target)
    })

#写出
with open('out.txt', "w", encoding="utf-8") as out_txt:
    out_txt.write(str(list_data))




