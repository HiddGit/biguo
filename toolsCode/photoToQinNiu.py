# -*- coding:utf-8 -*-
import os
import random
import time

from qiniu import Auth, put_file, etag
import tkinter
from tkinter import *
from tkinter.filedialog import askdirectory
import threading
import qiniu.config


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()
        self.func = func
        self.args = args
        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)


class ToQinNiu:
    def __init__(self, pDirPath, text1, var, canvas, roots):

        self.pDirPath = pDirPath
        self.text1 = text1
        self.text1.delete(1.0, END)
        self.var = var
        self.canvas = canvas
        self.root = roots
        if not self.pDirPath.endswith("/"):
            self.pDirPath =self.pDirPath+ "/"
        pli = os.listdir(self.pDirPath)
        # print("do")
        # print(pli)
        x = len(pli)  # 未知p变量，可更改
        n = 0  # 180是矩形填充满的次数
        k = 0  # 显示值
        self.canvas.create_rectangle(2, 2, 360, 28, width=0, fill="white")
        fill_line = self.canvas.create_rectangle(2, 2, 0, 27, width=0, fill="green")
        self.var.set("0.0%")
        # ftxt = open(self.pDirPath+"rmSame.txt",mode="r+",encoding="utf8")
        if not os.path.exists(self.pDirPath+"rmSame.txt"):
            ccc = open(self.pDirPath+"rmSame.txt",mode="a+",encoding="utf8")
            ccc.close()

        ftxt = open(self.pDirPath+"rmSame.txt",mode="r+",encoding="utf8")
        lines = ftxt.readlines()

        # print(lines)

        ls = len(lines)
        for mp in pli:
            try:
                # print("start",mp)
                if self.is_img(os.path.splitext(mp)[1]) :
                    # print("lenlines",ls)
                    if ls !=0:
                        for line in lines:
                            if mp+"\n" == line:
                                print("yiyou")
                                self.text1.insert(END, "##已存在===" + mp + "\n")
                                self.text1.insert(END, "http://img.biguotk.com/" + mp + "\n\n")

                                break
                            elif mp+"\n" != line and line==lines[-1]:
                                newpath = self.pDirPath + mp
                                # print(mp,newpath,)
                                self.doing(mp,newpath)
                                # self.testdoing(mp, newpath)
                                self.text1.insert(END, "上传成功===" + newpath + "\n")
                                self.text1.insert(END, "http://img.biguotk.com/" + mp + "\n\n")

                                ftxt.write(mp+"\n")
                                ftxt.flush()
                                print("ftxt write success")
                    else:
                        newpath = self.pDirPath + mp
                        # print(mp,newpath,)
                        self.doing(mp,newpath)
                        # self.testdoing(mp, newpath)
                        self.text1.insert(END, "上传成功===" + newpath + "\n")
                        self.text1.insert(END, "http://img.biguotk.com/" + mp + "\n\n")

                        ftxt.write(mp + "\n")
                        ftxt.flush()
                        print("ftxt write success")



            except Exception as e:
                self.text1.insert(END, "the photo error===" + self.pDirPath + mp + "\t" + str(e) + "\n\n")
                # print("the photo is error==="+pDirPath+mp+"\n")
                continue
            n = n + 360 / x
            k = k + 100 / x
            # 以矩形的长度作为变量值更新
            self.canvas.coords(fill_line, (0, 0, n, 30))
            if k >= 100:
                self.var.set("100%")
            else:
                self.var.set(str(round(k, 1)) + "%")
            self.root.update()
        ftxt.close()
    def testdoing(self, a, b):
        print("testdoing", a, b)

    def is_img(self, ext):
        ext = ext.lower()
        if ext == '.jpg':
            return True
        elif ext == '.png':
            return True
        elif ext == '.jpeg':
            return True
        elif ext == '.gif':
            return True
        elif ext == '.bmp':
            return True
        elif ext == '.psd':
            return True
        elif ext == '.tiff':
            return True
        elif ext == '.tga':
            return True
        elif ext == '.eps':
            return True
        else:
            return False

    def doing(self, pName, pPath):
        access_key = 'ZddHMKyJzMggwZdaIkSnMzOkxv8TJpGpZRhsCBAN'
        secret_key = 'Yvh46TGnE5gXPT1u004S97lv9_xTrwfrSpb0zdbv'

        # 构建鉴权对象
        q = Auth(access_key, secret_key)

        # 要上传的空间
        bucket_name = 'biguotk'

        # 上传到七牛后保存的文件名
        key = pName

        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)

        # 要上传文件的本地路径
        localfile = pPath

        ret, info = put_file(token, key, localfile)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)


class PhotoToExcel:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("UpLoad Photos to Qinniu")
        # self.root.iconbitmap('./cm03.ico')
        sh = self.root.winfo_screenheight()
        sw = self.root.winfo_screenwidth()
        ww = 800
        wh = 650
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.fpath = StringVar()

        self.var = StringVar()
        self.run()

    def selectfPath(self):
        path_ = askdirectory()
        self.fpath.set(path_)

    def sure_path(self, ):
        get_fpath = self.fpath.get()

        ToQinNiu(get_fpath, self.text1, self.var, self.canvas, self.root)
        # Show_words(get_fpath, get_spath, num, self.text1, self.var, self.canvas, self.root)

    def run(self):
        frame0 = Frame(self.root)
        frame0.pack()
        Label(frame0, text="目标路径", width=10).grid(row=0, column=0, padx=5, pady=10)
        Entry(frame0, textvariable=self.fpath, width=50, font=("", 13, "")).grid(row=0, column=1, columnspan=4, pady=10)
        Button(frame0, text="选择文件夹", command=self.selectfPath, width=10).grid(row=0, column=5, padx=5, pady=10)

        Button(frame0, text="开始上传", command=lambda: MyThread(self.sure_path), width=20).grid(row=1,
                                                                                             column=5,
                                                                                             # columnspan=1,
                                                                                             padx=5,
                                                                                             pady=10,
                                                                                             )

        self.var.set("进度")
        self.jindu = Label(frame0, textvariable=self.var, width=10)
        self.jindu.grid(row=1, column=0, padx=5)
        self.canvas = Canvas(frame0, width=350, height=26, bg="white")
        # 创建一个矩形外边框（距离左边，距离顶部，矩形宽度，矩形高度），线型宽度，颜色
        self.out_line = self.canvas.create_rectangle(2, 2, 360, 27, width=1, outline="black")
        self.canvas.grid(row=1, column=1, columnspan=3, ipadx=5)

        frame1 = Frame(self.root, width=35)
        frame1.pack()

        s1 = Scrollbar(frame1)
        s1.pack(side=RIGHT, fill=Y)
        text1 = Text(frame1, height=28, width=100, font=("", 13, ""), yscrollcommand=s1.set)
        text1.pack(expand=YES, fill=BOTH, pady=10, side=RIGHT, padx=80)
        self.text1 = text1
        text1.insert(END,"\n\n\t注：图片仅支持 png/jpg/jpeg/bmg 格式 \n\n\t 生成的图片名后缀为 png ")
        s1.config(command=text1.yview)
        menubar = Menu(frame1)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Copy", command=self.copy)
        filemenu.add_command(label="Paste", command=self.paste)
        filemenu.add_command(label="Cut", command=self.cut)
        menubar.add_cascade(label="File", menu=filemenu)
        self.filemenu=filemenu
        # self.text1.bind("<Button-3>", self.popupmenu) #windows
        self.text1.bind("<Button-2>", self.popupmenu)   #mac


        frame2 = Frame(self.root, width=35)
        frame2.pack(pady=10)
        Button(frame2, text="生成图片名和标签", command=lambda: MyThread(self.generatePname), width=35).grid(row=0,
                                                                                           column=2,
                                                                                           columnspan=3,
                                                                                           padx=5,
                                                                                           pady=5,
                                                                                           sticky=N)

        self.root.mainloop()

    def popupmenu(self,event):
        self.filemenu.post(event.x_root, event.y_root)
    def cut(self,event=None):
        self.text1.event_generate("<<Cut>>")
    def copy(self,event=None):
        self.text1.event_generate("<<Copy>>")
    def paste(self,event=None):
        self.text1.event_generate('<<Paste>>')
    def generatePname(self):
        self.text1.delete(1.0,END)
        for n in range(10):
            pName = str("{:.7f}".format(time.time()))
            a = chr(random.randrange(65, 65 + 26))
            b = chr(random.randrange(65, 65 + 26))
            pName = pName.replace(".",a+b) +".png"
            self.text1.insert(END,pName+"\n")
            imgsr = '<img src="http://img.biguotk.com/'+pName+'" />'
            self.text1.insert(END,imgsr+ "\n\n")
            time.sleep(0.012)
        pass



if __name__ == '__main__':
    PhotoToExcel()
    pass