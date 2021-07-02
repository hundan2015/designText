from bs4 import BeautifulSoup
import requests
import time
from step_search import step_s

#这是关键词
keyword = '硕士'
ans = []

s = time.perf_counter()
with open("wordhub.txt", "r", encoding="utf-8") as in_txt:
    wordlist = eval(in_txt.readline())

if keyword in wordlist:
    print('keyword detected')
    filename = 'hot_result/' + keyword + '.txt'
    with open(filename, "r", encoding="utf-8") as in_txt1:
        ans = eval(in_txt1.readline())
    in_txt1.close()

# print(ans)
# print(type(ans))
#ans就是列表类型的数据 是返回的内容
print('响应时间{}秒'.format(time.perf_counter() - s))
in_txt.close()

#input('Press Enter to exit...')
