from flask import Flask, request,jsonify,render_template
import json
from flask_cors import CORS
app = Flask(__name__,static_folder="./templates",static_url_path="")
app.config['JSON_AS_ASCII'] = False
from bs4 import BeautifulSoup
import requests
import time
from step_search import step_s

CORS(app)

@app.route("/")
def page():
    return render_template("index.html")

@app.route("/SSearcher/upload",methods=["POST"])
def SpiderCore():
    keyword = json.loads(request.get_data(as_text=True))
    print(keyword)
    keyword = keyword[0]["tar"]
    ans = []
    s = time.perf_counter()
    with open("wordhub.txt", "r", encoding="utf-8") as in_txt:
        wordlist = eval(in_txt.readline())

    if keyword in wordlist:
        print('keyword detected')
        filename = 'hot_result/' + keyword + '.txt'
        with open(filename, "r", encoding="utf-8") as in_txt:
            ans = eval(in_txt.readline())

    # print(ans)
    # print(type(ans))
    #ans就是列表类型的数据 是返回的内容
    print('响应时间{}秒'.format(time.perf_counter() - s))
    shit=jsonify(ans)
    return shit
    #input('Press Enter to exit...')