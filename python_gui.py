#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from SSHConnection import SSHConnection
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
        
        #创建一个顶级菜单
        menubar = Menu(self.top)

        # 创建另一个下拉菜单“File”，然后将它添加到顶级菜单中
        editmenu = Menu(menubar, tearoff=False)
        editmenu.add_command(label="连接", command=self.Command5_Cmd)
        editmenu.add_command(label="Exit", command=self.Command6_Cmd)
        menubar.add_cascade(label="File", menu=editmenu)

        #显示菜单
        self.top.config(menu = menubar)
        
        labelY = 0.05
        labelW = 0.2
        labelH = 0.05
        spaceH = 0.05
        col = 4
        labelX = (1-labelW*col)/(col+1) 
        
        sshData = ["输入IP", "输入密码"]
        self.sshText = []
        for i in range(0,len(sshData)):
            tempX = i%col*(labelX+labelW)+labelX
            tempY = int(i/col)*(labelY+spaceH)+labelY
            tempLabel = Label(self.top, text=sshData[i%len(sshData)])
            tempLabel.place(relx=tempX, rely=tempY, relwidth=labelW, relheight=labelH)
            tempText = Text(self.top)
            tempText.place(relx=tempX, rely=tempY+labelH, relwidth=labelW,relheight=labelH)
            self.sshText.append(tempText)
        
        labelData = ["速度","CAN0时序","CAN1波特率","右转弯","刹车"]
        self.comboData = [["1","10","100","1000","10000","20000","50000","80000"],
                     ["2","10","100","1000","10000","20000","50000","80000"],
                     ["3","10","100","1000","10000","20000","50000","80000"],
                     ["4","10","100","1000","10000","20000","50000","80000"],
                     ["5","10","100","1000","10000","20000","50000","80000"],
                     ["6","10","100","1000","10000","20000","50000","80000"],
                     ["7","10","100","1000","10000","20000","50000","80000"],
                     ["8","10","100","1000","10000","20000","50000","80000"]]
        comboDefaultSelect = [0,0,0,0,0,0,0,0]
        self.comboList = []
        for i in  range(0,len(labelData)):
            tempX = i%col*(labelX+labelW)+labelX
            tempY = int(i/col)*(labelY+spaceH)+labelY+(labelY+labelH)*2
            tempLabel = Label(self.top, text=labelData[i])
            tempLabel.place(relx=tempX, rely=tempY, relwidth=labelW, relheight=labelH)
            ind = i
            tempCombo = Combobox(self.top, text=self.comboData[ind][0], values=self.comboData[i], font=('宋体',9))
            tempCombo.place(relx=tempX, rely=tempY+labelH, relwidth=labelW)
            tempCombo.current(comboDefaultSelect[i])
            self.comboList.append(tempCombo)
        
        
        List1Font = Font(font=('宋体',9))
        self.List1 = ScrolledText(self.top, font=List1Font)
        self.List1.place(relx=0.12, rely=4*(labelY+spaceH)+labelY, relwidth=0.76, relheight=0.3)
        self.List1.insert(END,"请点击预览查看命令列表")
        self.ListData = []
        
        btnData = ["读取原配置","重启","运行","预览"]
        clickData = [self.Command1_Cmd,self.Command2_Cmd,self.Command3_Cmd,self.Command4_Cmd]
        for i in range(0,len(btnData)):
            tempX = i%col*(labelX+labelW)+labelX
            tempBtn = Button(self.top, text=btnData[i], command=clickData[i])
            tempBtn.place(relx=tempX, rely=4*(labelY+spaceH+labelY)+0.3, relwidth=labelW, relheight=labelH)
        

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self._tk = master

    def Command1_Cmd(self, event=None):
        # print("保存")
        # showinfo("保存","敬请期待！")
        stdout = os.system("sudo ip -details -statistics link show can0")
        lines_iterator = iter(stdout.readline, b"")
        for item in lines_iterator:
            self.List1.insert(END,item+"\n")
            
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
            self.executeShell()
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
                         u"echo 'can1 set success!'"]
        self.List1.delete(1.0,END)
        for item in self.ListData:
            self.List1.insert(END,item+"\n")
        pass
    
    def executeShell(self):
        str = ';'.join(self.ListData)
        os.system(str)
        #运行后自动关闭窗口
        # self._tk.destroy();
        pass
    
    def Command5_Cmd(self, event=None):
        # showinfo("连接","敬请期待！")
        self.conn = SSHConnection(self.sshText[0].get(0.0,END), 22, 'titan', self.sshText[1].get(0.0,END),self)
        
        pass
    
    def Command6_Cmd(self, event=None):
        # showinfo("Exit","敬请期待！")
        self._tk.destroy()
        pass
    
    def show(self, message):
        showinfo("连接",message)
        

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()






