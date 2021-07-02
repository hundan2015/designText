from bs4 import BeautifulSoup
import requests

#对于具体网址返回基站网址
def getserver(s : str):
    dir = s.find('cn/')
    return s[:dir+3]

def get_html(seed : str):#从网址返回html
    req = requests.get(url = seed)
    html = req.text
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
    title = head.text
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
    except:
        pass
    a = a[1:-1]#去掉两边方括号
    list.append(a)

    return list
