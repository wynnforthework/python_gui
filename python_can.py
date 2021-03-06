#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import threading
import paramiko
from subprocess import Popen, PIPE
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
        winWidth = 900
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
        self.createWidgets()  #声明变量

    def createWidgets(self):
        self.top = self.winfo_toplevel()  #声明窗口名称

        labelY = 0.05
        labelW = 0.08
        labelH = 0.05
        spaceH = 0.1
        col = 10
        labelX = (1-labelW*col)/(col+1)
        labelData = ["can0","速度","加速度","左转弯","右转弯","刹车","油门","灯光","喇叭"]
        self.can0Text = []
        for i in  range(0,10):
            tempX = i%col*(labelX+labelW)+labelX
            tempY = int(i/col)*(labelY+spaceH)+labelY
            tempLabel = Label(self.top, text=labelData[i%len(labelData)])
            tempLabel.place(relx=tempX, rely=tempY, relwidth=labelW, relheight=labelH)
            if(i%col==0):
                continue
            ind = i-1
            tempText = Text(self.top)
            tempText.place(relx=tempX, rely=tempY+labelH, relwidth=labelW,relheight=labelH)
            self.can0Text.append(tempText)
            
        
        labelData = ["can1","速度","加速度","左转弯","右转弯","刹车","油门","灯光","喇叭"]
        self.can1Text = []
        for i in  range(0,10):
            tempX = i%col*(labelX+labelW)+labelX
            tempY = int(i/col)*(labelY+spaceH)+labelY+labelY+spaceH
            tempLabel = Label(self.top, text=labelData[i%len(labelData)])
            tempLabel.place(relx=tempX, rely=tempY, relwidth=labelW, relheight=labelH)
            if(i%col==0):
                continue
            ind = i-1
            tempText = Text(self.top)
            tempText.place(relx=tempX, rely=tempY+labelH, relwidth=labelW,relheight=labelH)
            self.can1Text.append(tempText)
        
        
        self.text_options = {"state": "disabled",
                             "fg": "#08c614",
                             "insertbackground": "#08c614",
                             "selectbackground": "#f01c1c"}
        can0Title = Label(self.top, text="can0")
        can0Title.place(relx=labelX, rely=1-0.6, relwidth=labelW, relheight=labelH)
        self.can0 = ScrolledText(self.top, **self.text_options)
        self.can0.place(relx=labelX, rely=1-0.5, relwidth=0.4, relheight=0.3)
        
        btnData = ["开始","清除","结束"]
        clickData = [self.Command1_Cmd,self.Command2_Cmd,self.Command3_Cmd]
        for i in range(0,len(btnData)):
            tempX = i%col*(labelX+labelW)+labelX
            tempBtn = Button(self.top, text=btnData[i], command=clickData[i])
            tempBtn.place(relx=tempX, rely=1-0.1, relwidth=labelW, relheight=labelH)

        can1Title = Label(self.top, text="can1")
        can1Title.place(relx=labelX+0.5, rely=1-0.6, relwidth=labelW, relheight=labelH)
        self.can1 = ScrolledText(self.top, **self.text_options)
        self.can1.place(relx=labelX+0.5, rely=1-0.5, relwidth=0.4, relheight=0.3)

        clickData = [self.Command4_Cmd,self.Command5_Cmd,self.Command6_Cmd]
        for i in range(0,len(btnData)):
            tempX = i%col*(labelX+labelW)+labelX+0.5
            tempBtn = Button(self.top, text=btnData[i], command=clickData[i])
            tempBtn.place(relx=tempX, rely=1-0.1, relwidth=labelW, relheight=labelH)
        
        self.canType = 0
        self.command = ""  
        self.popen = None     # will hold a reference to a Popen object
        self.running = False  # True if the process is running

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self._tk = master

    def Command1_Cmd(self, event=None):
        # print("保存")
        self.canType = 0
        self.text = self.can0
        self.command ="cansend can0 %s#%s%s%s%s%s%s%s%s"  %(self.can0Text[0].get(0.0,END),self.can0Text[1].get(0.0,END),self.can0Text[2].get(0.0,END),self.can0Text[3].get(0.0,END),self.can0Text[4].get(0.0,END),self.can0Text[5].get(0.0,END),self.can0Text[6].get(0.0,END),self.can0Text[7].get(0.0,END),self.can0Text[8].get(0.0,END))
        #self.start_thread()
        out = self.conn.exec_command("candump can0")
        self.show(out)
        pass

    def Command2_Cmd(self, event=None):
        # print("重启")
        self.canType = 0
        self.text = self.can0
        self.conn = SSHConnection('192.168.0.114', 22, 'titan', 'titan3',self)
        #self.command = "ifconfig"
        #self.clear()
        #self.start_thread()
        pass

    def Command3_Cmd(self, event=None):
        # print("运行")
        #self.canType = 1
        #self.stop()
        self.canType = 0
        self.text = self.can0
        self.command = "candump can0"
        self.start_thread(self)
        pass
    
    def Command4_Cmd(self, event=None):
        # print("预览")
        self.canType = 0
        self.text = self.can0
        self.command = "titan4"
        self.start_thread(self)
        pass
    
    def Command5_Cmd(self, event=None):
        # print("运行")
        self.canType = 0
        self.text = self.can0
        self.clear()
        pass
    
    def Command6_Cmd(self, event=None):
        # print("预览")
        self.stop()
        pass

    def executeShell(self):
        str = ';'.join(self.ListData)
        os.system(str)
        #运行后自动关闭窗口
        # self._tk.destroy();
        pass

    def clear_text(self):
        """Clears the Text widget"""
        self.text.config(state="normal")
        self.text.delete(1.0, "end-1c")
        self.text.config(state="disabled")

    def clear_entry(self):
        """Clears the Entry command widget"""
        self.entry.delete(0, "end")

    def clear(self, event=None):
        """Does not stop an eventual running process,
        but just clears the Text and Entry widgets."""
        self.clear_text()

    def show(self, message):
        """Inserts message into the Text wiget"""
        self.text.config(state="normal")
        self.text.insert("end", message)
        self.text.see("end")
        self.text.config(state="disabled")

    def start_thread(self, event=None):
        """Starts a new thread and calls process"""
        self.stop()
        self.running = True
        # self.process is called by the Thread's run method
        threading.Thread(target=self.process).start()

    def process(self):
        """Runs in an infinite loop until self.running is False""" 
        while self.running:
            self.execute()

    def stop(self):
        """Stops an eventual running process"""
        if self.popen:
            try:
                self.popen.kill()
            except ProcessLookupError:
                pass 
        self.running = False

    def execute(self):
        """Keeps inserting line by line into self.text
        the output of the execution of self.command"""
        try:
            # self.popen is a Popen object
            # self.popen = Popen(self.command.split(), stdout=PIPE, bufsize=1)
            # lines_iterator = iter(self.popen.stdout.readline, b"")

            # # poll() return None if the process has not terminated
            # # otherwise poll() returns the process's exit code
            # while self.popen.poll() is None:
            #     for line in lines_iterator:
            #         self.show(line.decode("utf-8", 'ignore'))
            # self.show("Process " + self.command  + " terminated.\n\n")

            if self.conn._client is None:
                self.conn._client = paramiko.SSHClient()
                self.conn._client._transport = self.conn._transport
            stdin, stdout, stderr = self.conn._client.exec_command(self.command)
            lines_iterator = iter(stdout.readline, b"")

            while stdout.closed is False:
                for line in lines_iterator:
                    self.show(line)
            self.show("Process " + self.command  + " terminated.\n\n")

        except FileNotFoundError:
            self.show("Unknown command: " + self.command + "\n\n")                               
        except IndexError:
            self.show("No command entered\n\n")

        self.stop()

class SSHConnection(object):
    def __init__(self, host, port, username, password,master):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._tk = master
        self._connect()  # 建立连接

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport
        self._tk.show("连接成功\n")

    #下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    #上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    #执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)

        data = stdout.read()
        if len(data) > 0:
            #print (data.strip())   #打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            #print (err.strip())    #输出错误结果
            return err

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
