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
    from tkinter.scrolledtext import ScrolledText
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
        winHeight = 600
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

        labelX = 0.12
        labelY = 0.05
        labelW = 0.1
        labelH = 0.05
        spaceH = 0.15
        col = 4;
        labelData = ["速度","加速度","左转弯","右转弯","刹车","油门","灯光","喇叭"];
        self.comboData = [["1","10","100","1000","10000","20000","50000","80000"],
                     ["2","10","100","1000","10000","20000","50000","80000"],
                     ["3","10","100","1000","10000","20000","50000","80000"],
                     ["4","10","100","1000","10000","20000","50000","80000"],
                     ["5","10","100","1000","10000","20000","50000","80000"],
                     ["6","10","100","1000","10000","20000","50000","80000"],
                     ["7","10","100","1000","10000","20000","50000","80000"],
                     ["8","10","100","1000","10000","20000","50000","80000"]];
        comboDefaultSelect = [0,0,0,0,0,0,0,0];
        btnData = ["保存","重启","运行","预览"];
        clickData = [self.Command1_Cmd,self.Command2_Cmd,self.Command3_Cmd,self.Command4_Cmd];
        self.comboList = []
        for i in  range(0,len(labelData)):
            tempX = i%col*(labelX+labelW)+labelX
            tempY = int(i/col)*(labelY+spaceH)+labelY
            tempLabel = Label(self.top, text=labelData[i])
            tempLabel.place(relx=tempX, rely=tempY, relwidth=labelW, relheight=labelH)
            ind = i
            tempCombo = Combobox(self.top, text=self.comboData[ind][0], values=self.comboData[i], font=('宋体',9))
            tempCombo.place(relx=tempX, rely=tempY+labelH, relwidth=labelW)
            tempCombo.current(comboDefaultSelect[i])
            self.comboList.append(tempCombo)
        
        
        List1Font = Font(font=('宋体',9))
        self.List1 = ScrolledText(self.top, font=List1Font)
        self.List1.place(relx=labelX, rely=2*(labelY+spaceH)+labelY, relwidth=0.76, relheight=0.3)
        self.List1.insert(END,"请点击预览查看命令列表")
        self.ListData = []
        
        for i in range(0,len(btnData)):
            tempX = i%col*(labelX+labelW)+labelX
            tempBtn = Button(self.top, text=btnData[i], command=clickData[i])
            tempBtn.place(relx=tempX, rely=2*(labelY+spaceH+labelY)+0.3, relwidth=labelW, relheight=labelH)
        

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        # print("保存")
        showinfo("保存","敬请期待！")
        pass

    def Command2_Cmd(self, event=None):
        # print("重启")
        showinfo("重启","敬请期待！")
        pass

    def Command3_Cmd(self, event=None):
        # print("运行")
        if(len(self.ListData)==0):
            showwarning("运行","请先预览")
        else:
            self.shellIndex = 0
            self.executeShell();
        pass
    
    def Command4_Cmd(self, event=None):
        # print("预览")
        self.ListData = [u"sudo -S ifconfig <<EOF",
                         u"titan3",
                         u"EOF",
                         u"sudo ifconfig eth0 multicast",
                         u"sudo route add -net 224.0.0.0 netmask 240.0.0.0 dev eth0",
                         u"sudo modprobe can",
                         u"echo 'can success!'",
                         u"sudo modprobe can_raw",
                         u"echo 'can_raw success!'",
                         u"sudo modprobe can_dev",
                         u"echo 'can_dev success!'",
                         u"sudo modprobe mttcan",
                         u"echo 'mttcan success!'",
                         u"sudo ip link set can0 type can bitrate %s" % self.comboData[1][self.comboList[1].current()],
                         u"echo 'can0 bitrate is %s'" % self.comboData[1][self.comboList[1].current()],
                         u"sudo ip link set up can0",
                         u"echo 'can0 set success!'",
                         u"sudo ip link set can1 type can bitrate %s " % self.comboData[3][self.comboList[3].current()],
                         u"echo 'can1 bitrate is %s'" % self.comboData[3][self.comboList[3].current()],
                         u"sudo ip link set up can1",
                         u"echo 'can1 set success!'"];
        self.List1.delete(1.0,END)
        for item in self.ListData:
            self.List1.insert(END,item+"\n")
        pass
    
    def executeShell(self):
        if(self.shellIndex<len(self.ListData)):
            os.system(self.ListData[self.shellIndex])
            self.shellIndex += 1
            self.executeShell();
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()






