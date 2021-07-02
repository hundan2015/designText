from bs4 import BeautifulSoup
import requests
import time
import _thread
from step_search import step_s
seed = 'http://cos.neu.edu.cn/1132/list.htm'
keyword = '研究生'

s = time.perf_counter()
step_s.single_search_thread(seed, keyword)
print('多线程时间为{}'.format(time.perf_counter() - s))

s = time.perf_counter()
step_s.single_search(seed, keyword)
print('单线程时间为{}'.format(time.perf_counter() - s))

# test_time('1')
#input('Press Enter to exit...')
