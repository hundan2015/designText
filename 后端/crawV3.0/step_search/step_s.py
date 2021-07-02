#import turtle as t
#from datetime import datetime as d
#import math
#import random
import time
from bs4 import BeautifulSoup
import requests
import threading

#从单一的网址子网址查询关键词
#返回一个字典列表
#'TITLE': 'HREF': 'CONTEXT':

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, url, word, num):
        threading.Thread.__init__(self)
        self.url = url
        self.word = word
        self.num = num
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting line" + str(self.num))
        self.res = search_url(self.url, self.word, self.num)
        print("Exiting line" +  str(self.num))

def multiple_search(seed_list : list, word : str):
    list = []
    num = 1
    print('multiple_search {} \n {} start'.format(seed_list, word))
    # L_list = []
    for seeds in seed_list:
        list.extend(single_search_thread(seeds, word))
        print('single_search{} complete'.format(num))
        num += 1
    print('multiple_search {} {} end'.format(seed_list, word))
    return list


def single_search(seed:str, word:str):
    list = []
    # print('start single search')
    urllist = get_url(seed)
    # print('url list get!')
    num = 0
    for url in urllist:
        num += 1
        try:
            res = search_url(url, word, num)
        except:
            continue
        if res == 0:
            continue
        list.append(res)
    return list

def single_search_thread(seed:str, word:str):
    list = []
    # print('start single search')
    urllist = get_url(seed)
    # print('url list get!')
    num = 0
    thrs = []
    for i in range(urllist.__len__()):
        thread_t = myThread(urllist[i], word, i)
        thrs.append(thread_t)
        thrs[i].start()
        num += 1
    for x in thrs:
        try:
            res = x.res
        except:
            continue
        if res == 0:
            continue
        list.append(res)
    return list

def search_url(url : str,word : str ,num : int):
    l_url = get_content(url)

    #显示进度
    print('url{}'.format(num), end= ' ')
    if(num % 10 == 0):
        print()
    num += 1

    #加入搜索到的网址
    if word in l_url[0] or word == '':
        # list.append(url)
        if l_url[1].__len__() < 10:
            l_url[1] = '暂无内容 哎嘿~'
        if l_url[1].__len__() >100:
            l_url[1] = l_url[1][:200]
        dict = {
                    'TITLE':l_url[0],
                    'HREF':url,
                    'CONTEXT':l_url[1]
                }
        return dict
    else:
        return 0

def getserver(s : str):
    dir = s.find('cn/')
    return s[:dir+3]

def get_html(seed : str):#从网址返回html
    html = ''
    try:
        req = requests.get(url = seed)
        html = req.text
    except:
        pass
    return html

def get_url(seed : str):#从网址返回网址
    list = []
    server = getserver(seed)
    html = get_html(seed)

    div_bf = BeautifulSoup(html, features="html.parser")
    div = div_bf.find_all('a')
    for x in div:
        try:
            newurl = server + x.get('href')
        except:
            continue
        if(len(x.text) >= 4):
            list.append(newurl)
    return list

def get_content(seed: str):
    return html_content(get_html(seed))

#对html返回标题和内容
def html_content(html : str):#list[0]:title list[1]:context
    list = []
    div_bf = BeautifulSoup(html, features="html.parser")

    head = div_bf.find('title')
    # title = head.text
    try:
        title = head.text
        if title.__len__() <= 4:
            head = div_bf.find('title')
            title = head.text
    except:
        oo = ['empty','content']
        return oo
    list.append(title)

    div = div_bf.find_all('div', frag = '窗口9')
    try:
        if len(div[0].text) < 10:
            div = div_bf.find_all('div', frag = '窗口3')
    except:
        div = div_bf.find_all('div', frag = '窗口3')
    a = ''
    try:
        a = div[0].text.replace('\xa0'*8,'')
        a = div[0].text.replace('\xa0'*2,'')
    except:
        pass
    try:
        a = a.replace('\t'*4,' ')
        a = a.replace('\n\n','\n')
        a = a.replace('\u3000',' ')
    except:
        pass
    a = a[1:-1]#去掉两边方括号
    list.append(a)

    return list

def single_search_print(seed:str, word:str):
    list = []
    # print('start single search')
    urllist = get_url(seed)
    # print('url list get!')
    num = 1
    for url in urllist:
        l_url = ['','']
        l_url = get_content(url)

        #显示进度
        # print('url{}'.format(num), end= ' ')
        # if(num % 10 == 0):
        #     print()
        num += 1

        #加入搜索到的网址
        if word in l_url[0] or word == '':
            # list.append(url)
            print(type(l_url[1]))
            if l_url[1].__len__() < 10:
                l_url[1] = '暂无内容 哎嘿~'
            print('{} : {}'.format(l_url[0], url))
            if l_url[1].__len__() >200:
                l_url[1] = l_url[1][:200]
            list.append({
                'TITLE':l_url[0],
                'HREF':url,
                'CONTEXT':l_url[1]
            })
    return list

def multiple_search_print(seed_list : list, word : str):
    list = []
    num = 1
    # print('multiple_search {} \n {} start'.format(seed_list, word))
    # L_list = []
    for seeds in seed_list:
        list.extend(single_search_print(seeds, word))
        # print('single_search{} complete'.format(num))
        num += 1
    # print('multiple_search {} {} end'.format(seed_list, word))
    return list


#input('Press Enter to exit...')
