# -*- coding:utf-8 -*-
import random

import xlwt
import os
import re
import time
import requests



def generatePname():


    pName = str("{:.7f}".format(time.time()))
    a = chr(random.randrange(65, 65 + 26))
    b = chr(random.randrange(65, 65 + 26))
    c = chr(random.randrange(65, 65 + 26))
    d = chr(random.randrange(65, 65 + 26))
    pName = pName.replace(".", a + b+c+d)

    return  pName

# print(generatePname())
def toSaveImg(oneArry,sPath):
    for n in range(2, len(oneArry)):
        if oneArry[n] == "":
            continue
        else:
            try:
                mystrs = changeSrc(oneArry[n], sPath)
                if mystrs != "":
                    oneArry[n] = mystrs

            except Exception as e:
                print("my err", e)
                continue
    return oneArry

def changeSrc(srcStr,pPath):
    if not pPath.endswith("/"):
        pPath = pPath + "/"
    if re.findall(r"<img.*?src=[\"\'](.*?)[\"\'].*?>",srcStr):
        srcStr = re.sub(r"(<img).*?(src=[\"\'](.*?)[\"\']).*?>",r"\1 \2 />",srcStr)
        # print("    old src###",srcStr)
        # srcStr = re.sub(r"title=[\"\'].*?[\"\']","",srcStr)
        # srcStr = re.sub(r"alt=[\"\'].*?[\"\']","",srcStr)
        needpath = re.findall(r"<img.*?src=[\"\'](.*?)[\"\'].*?>",srcStr)
        for m in needpath:
            newName = generatePname()

            newName = newName + ".jpg"
            newPath = "http://img.biguotk.com/" + newName
            # print(" old",srcStr)
            downPhoto("http://www.edu-edu.com/exam-admin/home/my/admin/real/questionbank/question/attaches/"+m, pPath + newName)
            m = re.sub("\?","\?",m)
            srcStr = re.sub(m, newPath, srcStr)
            # print(" newstr",srcStr)
        # print("    new src###",srcStr)
        return srcStr

    else:
        return ""
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
        "Connection":"keep-alive",
        "Cookie": "JSESSIONID=A9D22FF2D797F13FFB1C2E8F24E7D979; JSESSIONID=30E3179DE363106BFCAF15821B73692E; JSESSIONID=E2DF64A8EAF57AE7741B074E5D02E501; service='http://www.edu-edu.com/sale/cas_security_check'; org.springframework.mobile.device.site.CookieSitePreferenceRepository.SITE_PREFERENCE=MOBILE; _tenant=default; JSESSIONID=4B20788FF7BE9377340DCBAE12238C03; JSESSIONID=8EDF39E271820A9B18F0F966D75D784B; JSESSIONID=8AC7EB6BBE0BCCDA935C47846DAF6BCC",
    }
    res = s.get(url,headers=headers)
    with open(savePath,mode="wb") as f :
        f.write(res.content)
        f.flush()
    # print("====ok save",savePath)
    # print("down over",savePath)
    return


def get_paper_arry():
    paper_array = [['序号', '类型', '问题', '选项A', '选项B', '选项C', '选项D', '选项E', '选项F', '正确答案', '解释']]
    return paper_array

def array11():
    array = []
    for i in range(1, 12):
        array.append('')
    return array


def write_xlsx(fpath, fname, con_list):  # 参数：('C:\work/',"2010年10月真题",conlist)
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'Tahoma'
    font.bold = False
    font.italic = False
    font.underline = False
    style.font = font
    if not os.path.exists(fpath):  # fname 为没有后缀名的
        os.mkdir(fpath)
    if not fpath.endswith("/"):  # 让fpath 是否带/都可以通过
        fpath = fpath + "/"
    filename = fname + '.xlsx'
    path = os.path.join(fpath, filename)
    if not os.path.exists(path):
        try:
            workbook = xlwt.Workbook(encoding='utf-8')
            worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
            for i in range(len(con_list)):
                for j in range(0, 11):
                    worksheet.write(i, j, con_list[i][j])

            workbook.save(path)
            print('写入<%s>excel完毕!' % fname)
        except Exception as e:
            print(e)
    else:
        print('<%s>文件已存在' % fname)

def change(num):
    num = int(num)
    if num == 0:
        return "A"
    elif num == 1:
        return "B"
    elif num == 2:
        return "C"
    elif num == 3:
        return "D"
    elif num == 4:
        return "E"
