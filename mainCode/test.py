# -*- coding:utf-8 -*-

import json
import requests
import re
import time
from lxml import etree
import json
import random

import xlwt
s = requests.session()
def downPhoto(url,savePath):
    headers = {
        "Host": "www.edu-edu.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.edu-edu.com/cas/web/login?service=http%3A%2F%2Fwww.edu-edu.com%2Fexam-admin%2Fcas_security_check&_tenant=default",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "JSESSIONID=CFB42D76DDFB74C61BA8BCCCB36729B6; _tenant=default; service='http://www.edu-edu.com/exam-admin/cas_security_check'; referer='http://www.edu-edu.com/cas/web/login?service=http%3A%2F%2Fwww.edu-edu.com%2Fexam-admin%2Fcas_security_check&_tenant=default'",
        "Connection":"keep-alive"
    }
    res = s.get(url,headers=headers)
    with open(savePath,mode="wb") as f :
        f.write(res.content)
        f.flush()
    # print("====ok save",savePath)
    return

if __name__ == '__main__':
    downPhoto("http://www.edu-edu.com/exam-admin/home/my/admin/real/questionbank/question/attaches/upload/file/28776/title?__id=QT7y5C45bBQ7Q94cj7g6.png","/Users/qiu60/Desktop/123.png")

    pass