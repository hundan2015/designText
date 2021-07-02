
s = 'http://aoff.whu.edu.cn/zsdt.htm'
def getserver(s : str):
    dir = s.find('cn/')
    return s[:dir+3]

print(getserver(s))
