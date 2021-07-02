# -*- coding:UTF-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def get_context(seed:str):
    print('get context {}'.format(seed))
    req = requests.get(url = seed)
    html = req.text
    print(html)
    div_bf = BeautifulSoup(html, features="html.parser")
    div = div_bf.find_all('div', class_ = 'article')
    # div = div_bf.find_all('div', id = 'section')
    div = str(div)
    div = div[1:-1]#去掉两边方括号
    return div

def get_word(seed:str):
    req = requests.get(url = seed)
    html = req.text
    div_bf = BeautifulSoup(html, features="html.parser")
    # div = div_bf.find_all('div', class_ = 'article')
    div = div_bf.find_all('div', frag = '窗口9')
    try:
        if len(div[0].text) < 10:
            div = div_bf.find_all('div', frag = '窗口3')
    except:
        div = div_bf.find_all('div', frag = '窗口3')
    a = ''
    try:
        a = div[0].text.replace('\xa0'*8,'')
        a = a.replace('\t'*4,' ')
        a = a.replace('\n'*2,' ')
    except:
        pass
    a = a[1:-1]#去掉两边方括号
    return a
