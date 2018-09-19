# -*- coding: utf-8 -*-
import requests
import time
import re
import json
from pymongo import MongoClient
from bs4 import BeautifulSoup
import csv

# url = "http://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649408965&idx=3&sn=e67b7c791a27b828b70bf0b7aae4a164&chksm=87f7c15eb0804848e1afca0fe93c64a4b6758da757c0a5b4cc7b9237baa4dae453ce4885b921#rd"
#从fillder 获取headers,包括cookie,反反爬虫机制
headers = '''
Host: mp.weixin.qq.com
Accept-Encoding: gzip, deflate
Cookie: devicetype=iPhoneOS9.0.2; lang=zh_CN; pass_ticket=GVG/6IdesXFQlzPwHd8lEUrixLhBKYXYouAFIWAfkP7sX65SBP+11kVRwq8G01oI; rewardsn=; version=16070026; wap_sid2=CPzW59gHElxkY3g1dEktZV9la0RUNG5CSWpfdDd6UGo3aFBzRWVGZU1ENHNiQ2JTMDFqNHBEQVZxUzBBOGhEM0twS0NscTZLeE1NX1c0OFd3dE9ESUV6WEJKZEJxTTBEQUFBfjDQrNXcBTgNQAE=; wxtokenkey=777; wxuin=2065296252
Connection: keep-alive
Accept: */*
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A452 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN
Referer: https://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649409395&idx=2&sn=d87db8de289ee2aa517079f8812649a7&chksm=87f7c3e8b0804afee2f56726116b8177e064d24ba00404ba3fa355c8793354b5f2ebd2332338&scene=4&ascene=0&devicetype=iPhone+OS9.0.2&version=16070026&nettype=WIFI&abtest_cookie=BAABAAgACgALABMABACehh4AI5ceAFuZHgBimR4AAAA%3D&lang=zh_CN&fontScale=100&pass_ticket=GVG%2F6IdesXFQlzPwHd8lEUrixLhBKYXYouAFIWAfkP7sX65SBP%2B11kVRwq8G01oI&wx_header=1
Accept-Language: zh-cn
X-Requested-With: XMLHttpRequest
'''

headers = headers.split("\n")
d_headers = dict()
for h in headers:
    if h:
        k, v = h.split(":", 1)
        d_headers[k] = v.strip()


def getDate(times):
    """毫秒转日期"""
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
    return date


# 获取评论和评论点赞数
def getComment(link):
    # 获得mid,_biz,idx,sn 这几个在文章url中的信息
    mid = link.split("&")[1].split("=")[1]
    idx = link.split("&")[2].split("=")[1]
    sn = link.split("&")[3].split("=")[1]
    _biz = link.split("&")[0].split("_biz=")[1]

    # 需要获取文章网页html 信息，设置cookie
    header = {
        "Cookie": "tvfe_boss_uuid=72565b9e745e0cef; pgv_pvid=8694301872; pgv_pvi=2146114560; ua_id=nRQrJ3t9QvibdVZNAAAAAGINM9KuieT13kzJrDf97Aw=; mm_lang=zh_CN; noticeLoginFlag=1; xid=89f92bc9546feef254b30c03c8b12ed4; openid2ticket_oj08H52SFiv5_1ix2PmIw_uoRlDQ=vUPcZ8S/zw7fzbv2SddnZkKlEfEfxYeMRM2nW5yx+qQ=; rewardsn=; wxtokenkey=777",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    web_data = requests.get(link, headers=header)
    Soup = BeautifulSoup(web_data.text,"html.parser")
    #利用正则提取comment_id
    pattern = re.compile(r"var comment_id = \"(.*?)\" \|\|")
    #print(pattern)
    script = Soup.find(text=pattern)
    #print(script)

    comment_id = pattern.search(script).group(1)
    # print(comment_id)

    # fillder 中取得一些不变得信息
    pass_ticket = "GVG%252F6IdesXFQlzPwHd8lEUrixLhBKYXYouAFIWAfkP7sX65SBP%252B11kVRwq8G01oI"
    appmsg_token = "973_Wie%2B0ppVwgdDrqMV9Yi2ZzkA4B2VUVaRYghrMclC_yuJX_fycOVWoZr11pdgnBZ45pjMScVpTh6VhRPk"

    # 目标url
    url = "https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment"

    # 添加data，`req_id`、`pass_ticket`分别对应文章的信息，从fiddler复制即可。
    """
    添加请求参数
    __biz对应公众号的信息，唯一
    mid、sn、idx分别对应每篇文章的url的信息，需要从url中进行提取
    key、appmsg_token从fiddler上复制即可
    pass_ticket对应的文章的信息，也可以直接从fiddler复制
    """
    params = {
        "scene":"0",
        "__biz": _biz,
        "appmsgid": mid,
        "sn": sn,
        "idx": idx,
        "comment_id": comment_id,
        "offset": "0",
        "limit":"100",
        "uin":"777",
        "key": "777",
        "pass_ticket": pass_ticket,
        "wxtoken":"777",
        "divecetype":"iPhone&nbsp;OS9.0.2",
        "appmsg_token": appmsg_token,
    }
    # 使用get方法进行提交
    comment = requests.get(url, params=params,headers=d_headers,verify=False).json()
    # 提取其中的阅读数和点赞数

    host = "127.0.0.1"
    port = 27017

    # 连接数据库
    client = MongoClient (host, port)
    # 建库
    Comment_Wx = client['Comment_Wx']
    wx_comment_sheet2 = Comment_Wx['wx_comment_sheet2']
    #数据表2 单独记录每篇文章评论数
    data2 = {
        "mid": mid,
        "url": link,
        "elected_comment_total_cnt": comment["elected_comment_total_cnt"],
    }
    wx_comment_sheet2.insert_one(data2)

    comment_list = []
    for comment in comment["elected_comment"]:
        data = {
            "nick_name": comment["nick_name"],
            "comment_content": comment["content"],
            "comment_like_num": comment["like_num"],
            "create_time":getDate(comment["create_time"]),
            "mid": mid,
            "url": link,
            "reply": comment["reply"]["reply_list"]
        }
        comment_list.append(data)

    # likeNum = content["appmsgstat"]["like_num"]

    # 歇10s，防止被封
    time.sleep(30)
    return comment_list

def putIntoMogo(urlList):
    """将频率信息写入数据库"""
    host = "127.0.0.1"
    port = 27017

    # 连接数据库
    client = MongoClient(host, port)
    # 建库
    Comment_Wx = client['Comment_Wx']
    # 建表
    wx_comment_sheet = Comment_Wx['wx_comment_sheet']

    # 存
    for message in urlList:
        wx_comment_sheet.insert_one(message)
    print("成功！")

def main():
    # url = "http://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649407650&idx=1&sn=3a690c5780ba394ff5420af7b39899f6&chksm=87f7c4"
    # print(getComment(url))
    # url = "http://mp.weixin.qq.com/s?__biz=MzA4NDI3NjcyNA==&mid=2649386190&idx=1&sn=304624e56ea0e2d35b67fa10612f6664&chksm=87f76855b080e14318f7d24c05a47e19f150fa3e8a5977d19316c40df477b46a279169b95438#rd"
    # # messageAllInfo = []
    # getComment(url)
    with open ('XinHuaShe_Read_Like_wjy.csv', encoding='utf-8', errors='ignore') as csv_file:
        F = csv.reader (csv_file)
        urls = [row[-1] for row in F]
        for url in enumerate(urls):
            if(int(url[0])> 1991):
                try:
                    commentInfo = getComment(url[-1])
                    print ("第%s条数据" %(int(url[0])))
                    putIntoMogo(commentInfo)
                except:
                    print("第%s数据有误" %(int(url[0])))

if __name__ == '__main__':
    main()

