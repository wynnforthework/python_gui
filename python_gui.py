#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else: #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # 设置窗口大小
        winWidth = 600
        winHeight = 400
        # 获取屏幕分辨率
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        
        # 设置主窗口标题
        self.master.title('叶')
        # 设置窗口初始位置在屏幕居中
        self.master.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.List1Var = StringVar(value='List1')
        self.List1Font = Font(font=('宋体',9))
        self.List1 = Listbox(self.top, listvariable=self.List1Var, font=self.List1Font)
        self.List1.place(relx=0.507, rely=0.132, relwidth=0.312, relheight=0.675)

        self.Command3Var = StringVar(value='运行')
        self.style.configure('TCommand3.TButton', font=('宋体',9))
        self.Command3 = Button(self.top, text='运行', textvariable=self.Command3Var, command=self.Command3_Cmd, style='TCommand3.TButton')
        self.Command3.setText = lambda x: self.Command3Var.set(x)
        self.Command3.text = lambda : self.Command3Var.get()
        self.Command3.place(relx=0.25, rely=0.593, relwidth=0.089, relheight=0.101)

        self.Command2Var = StringVar(value='重启')
        self.style.configure('TCommand2.TButton', font=('宋体',9))
        self.Command2 = Button(self.top, text='重启', textvariable=self.Command2Var, command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.135, rely=0.593, relwidth=0.082, relheight=0.101)

        self.Command1Var = StringVar(value='保存')
        self.style.configure('TCommand1.TButton', font=('宋体',9))
        self.Command1 = Button(self.top, text='保存', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.041, rely=0.626, relwidth=0.062, relheight=0.084)

        self.Combo8List = ['Add items in designer or code!',]
        self.Combo8Var = StringVar(value='Add items in designer or code!')
        self.Combo8 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo8Var, values=self.Combo8List, font=('宋体',9))
        self.Combo8.setText = lambda x: self.Combo8Var.set(x)
        self.Combo8.text = lambda : self.Combo8Var.get()
        self.Combo8.place(relx=0.345, rely=0.461, relwidth=0.055)

        self.Combo7List = ['Add items in designer or code!',]
        self.Combo7Var = StringVar(value='Add items in designer or code!')
        self.Combo7 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo7Var, values=self.Combo7List, font=('宋体',9))
        self.Combo7.setText = lambda x: self.Combo7Var.set(x)
        self.Combo7.text = lambda : self.Combo7Var.get()
        self.Combo7.place(relx=0.237, rely=0.461, relwidth=0.068)

        self.Combo6List = ['Add items in designer or code!',]
        self.Combo6Var = StringVar(value='Add items in designer or code!')
        self.Combo6 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo6Var, values=self.Combo6List, font=('宋体',9))
        self.Combo6.setText = lambda x: self.Combo6Var.set(x)
        self.Combo6.text = lambda : self.Combo6Var.get()
        self.Combo6.place(relx=0.128, rely=0.477, relwidth=0.068)

        self.Combo5List = ['Add items in designer or code!',]
        self.Combo5Var = StringVar(value='Add items in designer or code!')
        self.Combo5 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo5Var, values=self.Combo5List, font=('宋体',9))
        self.Combo5.setText = lambda x: self.Combo5Var.set(x)
        self.Combo5.text = lambda : self.Combo5Var.get()
        self.Combo5.place(relx=0.02, rely=0.477, relwidth=0.082)

        self.Combo4List = ['Add items in designer or code!',]
        self.Combo4Var = StringVar(value='Add items in designer or code!')
        self.Combo4 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo4Var, values=self.Combo4List, font=('宋体',9))
        self.Combo4.setText = lambda x: self.Combo4Var.set(x)
        self.Combo4.text = lambda : self.Combo4Var.get()
        self.Combo4.place(relx=0.325, rely=0.198, relwidth=0.062)

        self.Combo3List = ['Add items in designer or code!',]
        self.Combo3Var = StringVar(value='Add items in designer or code!')
        self.Combo3 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo3Var, values=self.Combo3List, font=('宋体',9))
        self.Combo3.setText = lambda x: self.Combo3Var.set(x)
        self.Combo3.text = lambda : self.Combo3Var.get()
        self.Combo3.place(relx=0.23, rely=0.214, relwidth=0.062)

        self.Combo2List = ['Add items in designer or code!',]
        self.Combo2Var = StringVar(value='Add items in designer or code!')
        self.Combo2 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo2Var, values=self.Combo2List, font=('宋体',9))
        self.Combo2.setText = lambda x: self.Combo2Var.set(x)
        self.Combo2.text = lambda : self.Combo2Var.get()
        self.Combo2.place(relx=0.128, rely=0.247, relwidth=0.075)

        self.Combo1List = ['Add items in designer or code!',]
        self.Combo1Var = StringVar(value='Add items in designer or code!')
        self.Combo1 = Combobox(self.top, text='Add items in designer or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('宋体',9))
        self.Combo1.setText = lambda x: self.Combo1Var.set(x)
        self.Combo1.text = lambda : self.Combo1Var.get()
        self.Combo1.place(relx=0.027, rely=0.214, relwidth=0.089)

        self.Label1Var = StringVar(value='Label1')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.top, text='Label1', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.05, rely=0.05, relwidth=0.075, relheight=0.068)

        self.Label2Var = StringVar(value='Label2')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',9))
        self.Label2 = Label(self.top, text='Label2', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.128, rely=0.132, relwidth=0.041, relheight=0.068)

        self.Label3Var = StringVar(value='Label3')
        self.style.configure('TLabel3.TLabel', anchor='w', font=('宋体',9))
        self.Label3 = Label(self.top, text='Label3', textvariable=self.Label3Var, style='TLabel3.TLabel')
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda : self.Label3Var.get()
        self.Label3.place(relx=0.223, rely=0.099, relwidth=0.062, relheight=0.084)

        self.Label4Var = StringVar(value='Label4')
        self.style.configure('TLabel4.TLabel', anchor='w', font=('宋体',9))
        self.Label4 = Label(self.top, text='Label4', textvariable=self.Label4Var, style='TLabel4.TLabel')
        self.Label4.setText = lambda x: self.Label4Var.set(x)
        self.Label4.text = lambda : self.Label4Var.get()
        self.Label4.place(relx=0.318, rely=0.099, relwidth=0.048, relheight=0.068)

        self.Label5Var = StringVar(value='Label5')
        self.style.configure('TLabel5.TLabel', anchor='w', font=('宋体',9))
        self.Label5 = Label(self.top, text='Label5', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda : self.Label5Var.get()
        self.Label5.place(relx=0.02, rely=0.346, relwidth=0.055, relheight=0.068)

        self.Label6Var = StringVar(value='Label6')
        self.style.configure('TLabel6.TLabel', anchor='w', font=('宋体',9))
        self.Label6 = Label(self.top, text='Label6', textvariable=self.Label6Var, style='TLabel6.TLabel')
        self.Label6.setText = lambda x: self.Label6Var.set(x)
        self.Label6.text = lambda : self.Label6Var.get()
        self.Label6.place(relx=0.128, rely=0.362, relwidth=0.062, relheight=0.068)

        self.Label7Var = StringVar(value='Label7')
        self.style.configure('TLabel7.TLabel', anchor='w', font=('宋体',9))
        self.Label7 = Label(self.top, text='Label7', textvariable=self.Label7Var, style='TLabel7.TLabel')
        self.Label7.setText = lambda x: self.Label7Var.set(x)
        self.Label7.text = lambda : self.Label7Var.get()
        self.Label7.place(relx=0.223, rely=0.329, relwidth=0.048, relheight=0.084)

        self.Label8Var = StringVar(value='Label8')
        self.style.configure('TLabel8.TLabel', anchor='w', font=('宋体',9))
        self.Label8 = Label(self.top, text='Label8', textvariable=self.Label8Var, style='TLabel8.TLabel')
        self.Label8.setText = lambda x: self.Label8Var.set(x)
        self.Label8.text = lambda : self.Label8Var.get()
        self.Label8.place(relx=0.331, rely=0.362, relwidth=0.048, relheight=0.051)

        self.Label9Var = StringVar(value='Label9')
        self.style.configure('TLabel9.TLabel', anchor='w', font=('宋体',9))
        self.Label9 = Label(self.top, text='Label9', textvariable=self.Label9Var, style='TLabel9.TLabel')
        self.Label9.setText = lambda x: self.Label9Var.set(x)
        self.Label9.text = lambda : self.Label9Var.get()
        self.Label9.place(relx=0.507, rely=0.05, relwidth=0.062, relheight=0.068)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()






