# -*- coding:utf-8 -*-


import json
from aip import AipOcr
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename
import threading
import xlwt
import os


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        self.func = func
        self.args = args
        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)

class Show_words:
    def __init__(self, fpath, spath, num, text1, var, canvas, roots):
        self.text1 = text1
        self.text1.delete(1.0, END)
        self.text1.insert(END, "正在转换，请稍等。。。\n\n")
        self.fpath = fpath
        self.spath = spath
        self.var = var
        self.canvas = canvas
        self.root = roots
        self.num = num
        self.run()

    def get_paper_arry(self):
        paper_array = [['序号', '类型', '问题', '选项A', '选项B', '选项C', '选项D', '选项E', '选项F', '正确答案', '解释']]
        return paper_array

    def return_str(self, jpgpath, num,notestr=""):
        # APP_ID = '11520740'
        # API_KEY = '521GEgknODenXagzC0eT3YKr'
        # SECRET_KEY = 'amBoDTB5oYLfmT9zsDvrmc2rdwwvESY8'
        APP_ID = '15107356'
        API_KEY = '0sx5APgxP6O7KCyxtNAPxhl7'
        SECRET_KEY = 'FQMcu7PjgT9xE7yInraiB000XdVqVNzZ'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        with open(jpgpath, 'rb') as fp:
            image = fp.read()
        # image = get_file_content(jpgpath)
        """ 如果有可选参数 """
        options = {}
        options["language_type"] = "CHN_ENG"
        """ 带参数调用通用文字识别（高精度版） """
        # try :   #500次高精度
        #     print("################高精度版")
        result = " "

        if num == 2:
            result = client.basicAccurate(image, options)
            notestr = "高精度转换----\t"

        # except:  #50000次普通
        if num == 1:
            result = client.basicGeneral(image, options)
            notestr = "普通转换----\t"
            print("putdsfafdsf")
        a = json.dumps(result["words_result"])
        b = json.loads(a)
        str11 = ""

        for i in b:
            content = i["words"]
            # print("all content",content)
            if re.findall(r"绝密★|浙江省|草稿纸|未涂均无分|本卷所有|试卷空白|考试时间|答题卡|本试卷|试题第\d页|试卷第\d页|答题区|全国教育|非选择题|自学考试|课程代码|判断正误|答题纸|选择题部分|注意事项|试题.*选涂其他|考试课程|涂黑", content) or \
                re.findall(r"^[四|五|六|七].*题\({0,1}\d{1,2}分\){0,1}$|案例分析",content):
                print("continue",content)
                continue

            if re.findall(r"^\d{1,2}[\.、]{0,1}|第\d{1,2}题|文言文阅读|现代文阅读|本大题", content):

                content = " #_#s" + content
                print(content)
                # print("#——#",content)
            elif re.findall(r"综合应用题",content):
                continue
            # print("nocon",content)
            str11 += content
        # print(str11)

        if str11 == "" and num == 2:
            # print("str11 00")
            notestr += "\n高精度转换失败，转为普通转换。。。\t\t"
            self.return_str(jpgpath, 1,notestr)

        return str11,notestr

    def array11(self):
        array = []
        for i in range(1, 12):
            array.append('')
        return array

    def write_xlsx(self, fpath, fname, con_list):  # 参数[:：]{0,1}('C:\work/',"2010年10月真题",conlist)
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
        if os.path.exists(path):
            os.remove(path)
        try:
            workbook = xlwt.Workbook(encoding='utf-8')
            worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
            for i in range(len(con_list)):
                for j in range(0, 11):
                    worksheet.write(i, j, con_list[i][j])

            workbook.save(path)
            # print('写入<%s>excel完毕!' % fname)
        except Exception as e:
            # print(e)
            pass
        finally:
            pass

    def run(self):
        if not re.findall(r"/$", self.fpath):
            self.fpath = self.fpath + "/"
        fli = os.listdir(self.fpath)


        x = len(fli)  # 未知变量，可更改
        n = 0  # 180是矩形填充满的次数
        k = 0  # 显示值
        self.canvas.create_rectangle(2, 2, 360, 28, width=0, fill="white")
        fill_line = self.canvas.create_rectangle(2, 2, 0, 27, width=0, fill="blue")
        self.var.set("0.0%")

        for f in fli:
            try:
                path2 = self.fpath + f + "/"
                lic = os.listdir(path2)
                try:
                    lic = sorted(lic, key=lambda x: eval(re.findall(r"_(\d{1,4})\.", x)[0]))
                except Exception:
                    pass
                str1 = ' '
                notestr1 = ""
                for f2 in lic:
                    # print(f2)
                    ppath = path2 + f2
                    try:
                        r_strli = self.return_str(ppath, self.num)
                        r_str = r_strli[0]
                        notestr1 = r_strli[1]
                        # print("r_str",r_str)
                        if re.findall(r"(答案及评分参考|参考答案及评分标准|答案及评分标准)", r_str):
                            # print("break")
                            break
                        if re.findall(r"\d{1,2}\.(A|B|C|D)\d{1,2}\.(A|B|C|D)\d{1,2}\.(A|B|C|D)", r_str):
                            # print("break2")
                            break
                    except Exception as e:
                        r_str = ""
                    str1 += r_str + " "
                self.text1.insert(END, notestr1)
                ###
                # print("str1", str1)
                # print("_______________", f)
                arry = self.to_excel(str1)
                self.write_xlsx(self.spath, f, arry)
                if len(arry) >=2:
                    self.text1.insert(END, f + "\t++成功++\n\n")
                    self.text1.insert(END, "存入" + "\t++成功++\n\n")

                else:
                    self.text1.insert(END, f + "\t--失败--\n\n")
                # self.text1.insert(END, needstr)
                n = n + 360 / x
                k = k + 100 / x
                # 以矩形的长度作为变量值更新
                self.canvas.coords(fill_line, (0, 0, n, 30))
                if k >= 100:
                    self.var.set("100%")
                else:
                    self.var.set(str(round(k, 1)) + "%")
                self.root.update()
            except Exception:
                pass

    def to_excel(self, strs):
        paper_array = self.get_paper_arry()
        mylist = re.split(" #_#s", strs)
        # print(mylist)
        title_num = 1
        # sssli = []
        pd= False
        dx = False
        mcjs = False
        tkt = False
        for a in mylist:
            piece_li = self.array11()
            # a = re.sub(r"^\d{1,3}[\.、]{0,1}", "", a).replace(".", "#_#").replace("．", "#_#").replace("、", "#_#")
            # a = re.sub(r"^[\.、]", "", a)
            a = re.sub(r"^第\d{1,3}题", "", a)
            a = re.sub(r"^[\.、]", "", a)
            a = re.sub(r"\(本题\d{1,2}分\)", "", a)
            a = re.sub(r"\(\d{1,2}分\)", "", a)
            try:
                if re.findall(
                        r"\d{1,2}#_#[ABCD]\d{1,2}#_#[ABCD]\d{1,2}#_#[ABCD]|\d{1,2}\.[ABCD] {0,1}\d{1,2} {0,1}\.[ABCD] {0,1}\d{1,2}\.[ABCD]",
                        a) or a == "" or a == " #_#" or len(a) == 1:
                    continue
                if not re.findall(r"^\d{1,3}世纪|^\d{2,4}年", a):
                    a = re.sub(r"^\d{1,3}[\.、]{0,1}", "", a)
                a=a.replace(".", "#_#1#").replace("．", "#_#3#").replace("、","#_#2#").replace(
                    "\u200b", "").replace("\u3000", "").replace("\r", "").replace("\n", "").replace("\t", "").replace(
                    "&nbsp;", "").replace("\xa0", "")
                a = re.sub(r"^第\d{1,3}题", "", a)

                cls = 1
                que = ""
                chose_a = ""
                chose_b = ""
                chose_c = ""
                chose_d = ""
                chose_e = ""
                ans = ""
                any = ""
                # print("aaa",a)
                if re.findall(r"A#_#\d#", a) and re.findall("B#_#\d#", a) and re.findall("C#_#\d#", a) and re.findall("D#_#\d#", a):
                    cls = 1
                    if re.findall(r".*?\( {0,1}([ABCDE]{1,4} {0,1})\)", a):
                        ans = re.findall(r".*?\( {0,1}([ABCDE]{1,4} {0,1})\)", a)[0]
                        a = re.sub(r"(.*?)\( {0,1}([ABCDE]{1,4} {0,1})\)(.*)", r"\1( )\3", a)
                    elif re.findall(
                            r".*(【正确答案】[:：]{0,1}|【正确答案】|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答[:：]|答案要点[:：]{0,1}|答案[:：]{0,1}|【参考答案】|【答案】|正确答案|参考答案|答案|标准答案|正确答案是).*", a):
                        ans = \
                        re.findall(r"(【正确答案】[:：]{0,1}|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答[:：]|答案[:：]{0,1}|【正确答案】|【答案】|【参考答案】|正确答案|参考答案|答案|标准答案|正确答案是)(.*)",
                                   a)[0][1]
                        a = re.findall(
                            r"(.*?)(【正确答案】[:：]{0,1}|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答[:：]|答案[:：]{0,1}|【正确答案】|【答案】|【参考答案】|正确答案|参考答案|答案|标准答案|正确答案是)", a)[
                            0][0]

                    que = re.findall(r"(.*?)A#_#\d#", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                    chose_a = re.findall(r"A#_#\d#(.*?)B#_#\d#", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                    chose_b = re.findall(r"B#_#\d#(.*?)C#_#\d#", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                    chose_c = re.findall(r"C#_#\d#(.*?)D#_#\d#", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                    chose_d = re.findall(r"D#_#\d#(.*)", a)[0]
                    if dx == True:
                        cls =2
                    if re.findall(r"E#_#\d#", chose_d):
                        cls = 2
                        chose_e = re.findall(r"E#_#\d#(.*)", chose_d)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                        chose_d = re.findall(r"(.*?)E#_#\d#", chose_d)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")

                else:

                    if re.findall(r"A", a) and re.findall("B", a) and re.findall("C", a) and re.findall("D", a):
                        cls = 1

                        if re.findall(r".*?\( {0,1}([ABCDE]{1,4} {0,1})\)", a):
                            ans = re.findall(r".*?\( {0,1}([ABCDE]{1,4} {0,1})\)", a)[0]
                            a = re.sub(r"(.*?)\( {0,1}([ABCDE]{1,4} {0,1})\)(.*)", r"\1( )\3", a)
                        elif re.findall(r".*(【正确答案】[:：]{0,1}|【正确答案】|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答案[:：]{0,1}|答[:：]|【参考答案】|【答案】|正确答案|参考答案|答案|标准答案|正确答案是).*",
                                a):
                            ans = \
                                re.findall(
                                    r"(【正确答案】[:：]{0,1}|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答案[:：]{0,1}|答[:：]|【正确答案】|【答案】|【参考答案】|正确答案|参考答案|答案|标准答案|正确答案是)(.*)",
                                    a)[0][
                                    1]
                            a = \
                                re.findall(
                                    r"(.*?)(【正确答案】[:：]{0,1}|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答案[:：]{0,1}|答[:：]|【正确答案】|【答案】|【参考答案】|正确答案|参考答案|答案|标准答案|正确答案是)",
                                    a)[
                                    0][0]
                        que = re.findall(r"(.*?)A", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                        chose_a = re.findall(r"A(.*?)B", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                        chose_b = re.findall(r"B(.*?)C", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                        chose_c = re.findall(r"C(.*?)D", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                        chose_d = re.findall(r"D(.*)", a)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                        if dx == True:
                            cls =2
                        if re.findall(r"E", chose_d):
                            cls = 2
                            chose_e = re.findall(r"E(.*)", chose_d)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                            chose_d = re.findall(r"(.*?)E", chose_d)[0].replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                    else:
                        cls = 4
                        que = a

                        if re.findall(r".*(【正确答案】[:：]{0,1}|【正确答案】|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答案[:：]{0,1}|答[:：]|【参考答案】|【答案】|正确答案|参考答案|答案|标准答案|正确答案是).*",
                                a):
                            ans = \
                                re.findall(
                                    r"(【正确答案】[:：]{0,1}|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答案[:：]{0,1}|答[:：]|【正确答案】|【答案】|【参考答案】|正确答案|参考答案|答案|标准答案|正确答案是)(.*)",
                                    a)[0][
                                    1]
                            que = \
                                re.findall(
                                    r"(.*?)(【正确答案】[:：]{0,1}|参考答案[:：]{0,1}|正确答案[:：]{0,1}|答案要点[:：]{0,1}|答案[:：]{0,1}|答[:：]{0,1}|【正确答案】|【答案】|【参考答案】|正确答案|参考答案|答案|标准答案|正确答案是)",
                                    a)[
                                    0][0]
                        if pd==True:
                            cls = 3
                            chose_a = "是"
                            chose_b = "不是"
                        elif tkt:
                            cls = 5
                        elif mcjs:
                            cls = 8

                # print("que====",que,len(que))
                # sssli.append(que)
                if re.findall(r"单项选择题|试题.*选涂其他",que) or que == "" or len(que) == 0 or len(que)==1 or que== '  ' :
                    continue
                elif re.findall(r"多项选择",que):
                    dx = True
                    pd= False
                    mcjs = False
                    tkt = False
                    continue

                elif re.findall(r"判断.*本大题|判断题",que):
                    pd = True
                    dx=False
                    tkt = False
                    mcjs =False
                    continue
                elif re.findall(r"名词解释.*",que):
                    mcjs = True
                    dx=False
                    pd=False
                    tkt=False
                    continue
                elif re.findall(r"填空题.*",que):
                    tkt=True
                    mcjs = False
                    dx = False
                    pd = False
                    continue

                elif re.findall(r".*本大题",que):
                    dx = False
                    pd = False
                    mcjs=False
                    tkt=False
                    continue
                que = re.sub(r"^[\.、]", "", que)
                piece_li[0] = title_num
                piece_li[1] = cls
                piece_li[2] = que.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[2] = re.sub(r"^[\.、]","",piece_li[2])

                piece_li[3] = chose_a.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[3] = re.sub(r"^[\.]", "",piece_li[3])

                piece_li[4] = chose_b.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[4] = re.sub(r"^[\.、]","", piece_li[4])

                piece_li[5] = chose_c.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[5] = re.sub(r"^[\.、]","", piece_li[5])

                piece_li[6] = chose_d.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[6] = re.sub(r"^[\.、]","", piece_li[6])

                piece_li[7] = chose_e.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[7] = re.sub(r"^[\.、]", "",piece_li[7])

                piece_li[9] = ans.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[9] = re.sub(r"^[\.、]", "",piece_li[9])

                piece_li[10] = any.strip().replace("#_#1#", ".").replace("#_#2#", "、").replace("#_#3#", "．")
                piece_li[10] = re.sub(r"^[\.、]","", piece_li[10])
                # piece_li[10] = any
                print(piece_li)
                paper_array.append(piece_li)
                title_num += 1
            except Exception as e:
                # print("anystr err", e)
                self.text1.insert(END,"err")
                pass
        # print(paper_array)
        # print(sssli)
        return paper_array

class PhotoToExcel:



    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Photo To Excel")
        sh = self.root.winfo_screenheight()
        sw = self.root.winfo_screenwidth()
        ww = 800
        wh = 650
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.fpath = StringVar()
        self.spath = StringVar()
        self.var = StringVar()
        self.run()

    def selectfPath(self):
        path_ = askdirectory()
        self.fpath.set(path_)

    def selectsPath(self):
        spath_ = askdirectory()
        self.spath.set(spath_)

    def sure_path(self, num):
        get_fpath = self.fpath.get()
        get_spath = self.spath.get()
        Show_words(get_fpath, get_spath, num, self.text1, self.var, self.canvas, self.root)

    def run(self):
        frame0 = Frame(self.root)
        frame0.pack()
        Label(frame0, text="目标路径", width=10).grid(row=0, column=0, padx=5)
        Entry(frame0, textvariable=self.fpath, width=50, font=("", 13, "")).grid(row=0, column=1, columnspan=4)
        Button(frame0, text="选择文件夹", command=self.selectfPath, width=10).grid(row=0, column=5, padx=5)

        Label(frame0, text="存储路径", width=10).grid(row=1, column=0, padx=5, pady=5)
        Entry(frame0, textvariable=self.spath, width=50, font=("", 13, "")).grid(row=1, column=1, columnspan=4, pady=5)
        Button(frame0, text="选择文件夹/与上不同", command=self.selectsPath, width=20).grid(row=1, column=5, padx=5, pady=5)

        Button(frame0, text="普通转换", command=lambda: MyThread(self.sure_path, 1), width=35).grid(row=2, column=0,
                                                                                                columnspan=3, padx=5,
                                                                                                pady=5, sticky=N)

        Button(frame0, text="高精度转换（500张图/日）", command=lambda: MyThread(self.sure_path, 2), width=35).grid(row=2,
                                                                                                          column=3,
                                                                                                          columnspan=3,
                                                                                                          padx=5,
                                                                                                          pady=5,
                                                                                                          sticky=N)

        self.var.set("进度")
        self.jindu = Label(frame0, textvariable=self.var, width=10)
        self.jindu.grid(row=3, column=1, padx=5)
        self.canvas = Canvas(frame0, width=350, height=26, bg="white")
        # 创建一个矩形外边框（距离左边，距离顶部，矩形宽度，矩形高度），线型宽度，颜色
        self.out_line = self.canvas.create_rectangle(2, 2, 360, 27, width=1, outline="black")
        self.canvas.grid(row=3, column=2, columnspan=3, ipadx=5)

        frame1 = Frame(self.root, width=35)
        frame1.pack(side=LEFT)
        frame2 = Frame(self.root, width=35)
        frame2.pack(side=LEFT, padx=10)
        s1 = Scrollbar(frame1)
        s1.pack(side=RIGHT, fill=Y)
        text1 = Text(frame1, height=28, width=100, font=("", 13, ""), yscrollcommand=s1.set)
        text1.pack(expand=YES, fill=BOTH, pady=10, side=RIGHT, padx=80)
        self.text1 = text1
        s1.config(command=text1.yview)

        self.root.mainloop()


if __name__ == '__main__':
    PhotoToExcel()

    pass