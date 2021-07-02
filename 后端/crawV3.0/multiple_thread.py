from bs4 import BeautifulSoup
import requests
import time
import _thread
from step_search import step_s

def time_search():
    s = time.perf_counter()
    seed = 'http://www.cse.neu.edu.cn/6330/list1.htm'
    req = requests.get(url = seed)
    # print('使用{:.6f}秒'.format(time.perf_counter() - s))
    html = req.text
    print('使用{:.6f}秒'.format(time.perf_counter() - s))
    return time.perf_counter() - s

def test_time(s : str):
    a = 0
    k = 5
    for i in range(k):
        print('测试{}运行ing'.format(s))
        a += time_search()
    print('平均时间{:.6f}'.format(a/k))


try:
   _thread.start_new_thread( test_time, ("Thread-1",) )
   _thread.start_new_thread( test_time, ("Thread-2",) )
except:
   print ("Error: 无法启动线程")

while 1:
    pass
