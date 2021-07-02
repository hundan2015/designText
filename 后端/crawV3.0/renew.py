from bs4 import BeautifulSoup
import requests
from step_search import step_s

# seed = 'http://www.cse.neu.edu.cn/6330/list1.htm'
with open("search.txt", "r", encoding="utf-8") as in_txt:
    seed_list = eval(in_txt.readline())
in_txt.close()
print(seed_list)
keyword = ''
with open("wordhub.txt", "r", encoding="utf-8") as in_txt:
    wordlist = eval(in_txt.readline())
in_txt.close()
print(wordlist)
for words in wordlist:
    a = step_s.multiple_search(seed_list, words)
    poso = 'hot_result/' + words + '.txt'
    with open(poso, "w", encoding="utf-8") as out_txt:
        out_txt.write(str(a))
    out_txt.close()


#input('Press Enter to exit...')
'''
from bs4 import BeautifulSoup
import requests
from step_search import step_s

# seed = 'http://www.cse.neu.edu.cn/6330/list1.htm'
with open("search.txt", "r", encoding="utf-8") as in_txt:
    seed_list = eval(in_txt.readline())
print(seed_list)
keyword = ''
with open("wordhub.txt", "r", encoding="utf-8") as in_txt:
    wordlist = eval(in_txt.readline())
print(wordlist)
for words in wordlist:
    a = step_s.multiple_search(seed_list, words)
    poso = 'hot_result/' + words + '.txt'
    with open(poso, "w", encoding="utf-8") as out_txt:
        out_txt.write(str(a))


#input('Press Enter to exit...')'''
