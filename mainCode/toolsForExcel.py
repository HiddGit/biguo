# -*- coding:utf-8 -*-

import xlwt
import os
import re
import time
import requests


def changeSrc(srcStr,pPath):
    if not pPath.endswith("/"):
        pPath = pPath + "/"
    if re.findall(r"<img src=[\"\'](.*?)[\"\'].*?>",srcStr):
        print("    old src###",srcStr)
        srcStr = re.sub(r"title=[\"\'].*?[\"\']","",srcStr)
        srcStr = re.sub(r"alt=[\"\'].*?[\"\']","",srcStr)
        needpath = re.findall(r"<img src=[\"\'](.*?)[\"\'].*?>",srcStr)
        for m in needpath:
            timer = str(int(time.time()))

            newName = timer + "_" + re.findall(r".*/(.*\..*)", m)[0]
            newPath = "http://img.biguotk.com/" + newName
            srcStr = re.sub(m, newPath, srcStr)
            downPhoto(m,pPath+newName)

        print("    new src###",srcStr)
        return srcStr

    else:
        return ""

def downPhoto(url,savePath):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}
    res = requests.get(url,headers=headers)
    with open(savePath,mode="wb") as f :
        f.write(res.content)
        f.flush()
    # print("====ok save",savePath)
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
