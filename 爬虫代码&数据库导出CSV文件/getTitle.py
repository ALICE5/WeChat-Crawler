# -*- coding: utf-8 -*-
import requests
import time
import json
from pymongo import MongoClient


# 目标url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

Cookie = "tvfe_boss_uuid=72565b9e745e0cef; pgv_pvid=8694301872; pgv_pvi=2146114560; ua_id=nRQrJ3t9QvibdVZNAAAAAGINM9KuieT13kzJrDf97Aw=; mm_lang=zh_CN; noticeLoginFlag=1; pgv_si=s5643713536; uuid=f9b77e671eaa946bbfe86249b2c51fc0; bizuin=3876016015; ticket=68fb4a8e844a815258b41675d91e50614be622db; ticket_id=gh_f47f1017fdf9; cert=jMTZcMPoyHlFH4wNnFDmbi1kumj3ZXcb; data_bizuin=3876016015; data_ticket=cu9ukHSc5DPVtKwyWVoYb5YL/qFcawhBSybGt96dIDhCOSPWfLAdtPSlOQQIFttp; slave_sid=U1o1dlVOZmU2cEJYZWNmTlo0bDVwX2dEOE1YZWdYSll5RHdHcFpMbWxPYk84UE5CUHNNVUpKMElfRGRic29xZGd4T0pmUFJrWTlzSGM2cENmX0ZkZXBJazRXTHZuUmtScnVYRkE3dDF2aHcwVjlPM0JBWkpaRlJORlJhd2RwaEN6T1JtRTI4R3ZkdldvaHZF; slave_user=gh_f47f1017fdf9; xid=89f92bc9546feef254b30c03c8b12ed4; openid2ticket_oj08H52SFiv5_1ix2PmIw_uoRlDQ=vUPcZ8S/zw7fzbv2SddnZkKlEfEfxYeMRM2nW5yx+qQ="
# 使用Cookie，跳过登陆操作
headers = {
  "Cookie": Cookie,
  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}

"""
需要提交的data
以下个别字段是否一定需要还未验证。
注意修改yourtoken,number
number表示从第number页开始爬取，为5的倍数，从0开始。如0、5、10……
token可以使用Chrome自带的工具进行获取
fakeid是公众号独一无二的一个id，等同于后面的__biz
"""
data1 = {
    "token": "1256841906",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "action": "list_ex",
    "begin": "365",
    "count": "5",
    "query": "",
    "fakeid": "MzA4NDI3NjcyNA==",
    "type": "9",
}


# 毫秒数转日期
def getDate(times):
    # print(times)
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
    return date


# 获取阅读数和点赞数
def getMoreInfo(link):
    # 获得mid,_biz,idx,sn 这几个在link中的信息
    mid = link.split("&")[1].split("=")[1]
    idx = link.split("&")[2].split("=")[1]
    sn = link.split("&")[3].split("=")[1]
    _biz = link.split("&")[0].split("_biz=")[1]

    # fillder 中取得一些不变得信息
    req_id = "0816s2KUPsysbb4tlGi9Tzpu"
    pass_ticket = "hMc3%252Bja8kGgVeDvjeuAF8pH9RwqwH3oKpuI%252Bxy7uQDqhepkiOBB43QeQvXKODVGI"
    appmsg_token = "973_JPcELAzPNiLNj9r3bXKuvApILXHMLly98GiRrh-x5VI0epXKLjWLuAajUuo8qJUrac3_jfXfH_SXlzhv"

    # 目标url
    url = "http://mp.weixin.qq.com/mp/getappmsgext"
    # 添加Cookie避免登陆操作，这里的"User-Agent"最好为手机浏览器的标识
    headers = {
        "Cookie": "devicetype=iPhoneOS9.0.2; lang=zh_CN; pass_ticket=hMc3+ja8kGgVeDvjeuAF8pH9RwqwH3oKpuI+xy7uQDqhepkiOBB43QeQvXKODVGI; rewardsn=; version=16070026; wap_sid2=CLCZ54sDElxQanJnQnoyYUtoc1hiSlFMaEx2S01tb2U2LWNwSnQxWlN6aVc0MlZQdTRnZ01KdUROeW5SUTFrZWhiSzRVWU5JZTBwdk9JcER2eXpkR25PYjAySGhmTTBEQUFBfjDphs7cBTgNQAE=; wxtokenkey=777; wxuin=830065840",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 MicroMessenger/6.7.2 NetType/WIFI Language/zh_CN"
    }
    # 添加data，`req_id`、`pass_ticket`分别对应文章的信息，从fiddler复制即可。
    data = {
        "is_only_read": "1",
        "req_id": req_id,
        "pass_ticket": pass_ticket,
        "is_temp_url": "0",
    }
    """
    添加请求参数
    __biz对应公众号的信息，唯一
    mid、sn、idx分别对应每篇文章的url的信息，需要从url中进行提取
    key、appmsg_token从fiddler上复制即可
    pass_ticket对应的文章的信息，也可以直接从fiddler复制
    """
    params = {
        "__biz": _biz,
        "mid": mid,
        "sn": sn,
        "idx": idx,
        "key": "777",
        "pass_ticket": pass_ticket,
        "appmsg_token": appmsg_token,
    }

    # 使用post方法进行提交
    content = requests.post(url, headers=headers, data=data, params=params).json()
    # 提取其中的阅读数和点赞数
    # print(content["appmsgstat"]["read_num"], content["appmsgstat"]["like_num"])
    readNum = content["appmsgstat"]["read_num"]
    likeNum = content["appmsgstat"]["like_num"]

    # 歇10s，防止被封
    time.sleep(15)
    return readNum, likeNum


# 最大值365，所以range中就应该是73,15表示前3页
def getAllInfo(url, begin):
    # 拿一页，存一页
    messageAllInfo = []
    # begin 从0开始，365结束
    data1["begin"] = begin
    # 使用get方法进行提交
    content_json = requests.get(url, headers=headers, params=data1, verify=False).json()
    time.sleep(10)
    # 返回了一个json，里面是每一页的数据
    if "app_msg_list" in content_json:
        for item in content_json["app_msg_list"]:
            # 提取每页文章的标题及对应的url
            url = item['link']
            # print(url)
            readNum, likeNum = getMoreInfo(url)
            info = {
                "title": item['title'],
                "readNum": readNum,
                "likeNum": likeNum,
                "digest": item['digest'],
                "date": getDate(item['update_time']),
                "url": item['link']
            }
            messageAllInfo.append(info)
        return messageAllInfo


# 写入数据库
def putIntoMogo(urlList):
    host = "127.0.0.1"
    port = 27017

    # 连接数据库
    client = MongoClient(host, port)
    # 建库
    lianTong_Wx = client['lianTong_Wx']
    # 建表
    wx_message_sheet = lianTong_Wx['wx_message_sheet']

    # 存
    for message in urlList:
        wx_message_sheet.insert_one(message)
    print("成功！")

def main():
    # 出现问题,原因是频率太快 被封
    for i in range(350,351):
        begin = i*5
        messageAllInfo = getAllInfo(url, str(begin))
        print("第%s页" % i)

        putIntoMogo(messageAllInfo)

if __name__ == '__main__':
    main()
