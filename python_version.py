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

        #创建一个顶级菜单
        menubar = Menu(self.top)

        # 创建另一个下拉菜单“File”，然后将它添加到顶级菜单中
        editmenu = Menu(menubar, tearoff=False)
        editmenu.add_command(label="连接", command=self.Command5_Cmd)
        editmenu.add_command(label="Exit", command=self.Command6_Cmd)
        menubar.add_cascade(label="File", menu=editmenu)

        #显示菜单
        self.top.config(menu = menubar)

        sshData = ["输入IP", "输入密码"]
        self.sshText = []
        for i in range(0,len(sshData)):
            tempX = i%col*(labelX+labelW)+labelX
            tempY = 0
            tempLabel = Label(self.top, text=sshData[i%len(sshData)])
            tempLabel.place(relx=tempX, rely=tempY, relwidth=labelW, relheight=labelH)
            tempText = Text(self.top)
            tempText.place(relx=tempX, rely=tempY+labelH, relwidth=labelW,relheight=labelH)
            self.sshText.append(tempText)

        # 1.hostname/hosts配置
        label0 = Label(self.top, text="hostname/hosts")
        label0.place(relx=labelX, rely=0.15, relwidth=0.2, relheight=labelH)
        self.text0 = Text(self.top)
        self.text0.place(relx=0.2, rely=0.15, relwidth=0.2,relheight=labelH)
        btn0 = Button(self.top, text="配置", command=self.Command1_Cmd)
        btn0.place(relx=0.5, rely=0.15, relwidth=labelW, relheight=labelH)
        
        # 2.IP地址配置、VLAN配置
        label1 = Label(self.top, text="IP地址/VLAN")
        label1.place(relx=labelX, rely=0.25, relwidth=0.2, relheight=labelH)
        self.text1 = Text(self.top)
        self.text1.place(relx=0.2, rely=0.25, relwidth=0.2,relheight=labelH)
        btn1 = Button(self.top, text="配置", command=self.Command2_Cmd)
        btn1.place(relx=0.5, rely=0.25, relwidth=labelW, relheight=labelH)
        
        # 5.查看版本信息：内核/设备树/文件系统/FPGA
        label2 = Label(self.top, text="查看版本信息")
        label2.place(relx=labelX, rely=2*(labelY+spaceH)+labelY, relwidth=0.2, relheight=labelH)
        self.comboData = ["内核","设备树","文件系统","FPGA"]
        self.Combo = Combobox(self.top, text=self.comboData[0], values=self.comboData, font=('宋体',9))
        self.Combo.place(relx=0.2, rely=2*(labelY+spaceH)+labelY, relwidth=labelW)
        self.Combo.current(0)
        btn2 = Button(self.top, text="查看", command=self.Command3_Cmd)
        btn2.place(relx=0.5, rely=2*(labelY+spaceH)+labelY, relwidth=labelW, relheight=labelH)

        self.text_options = {"state": "disabled",
                             "fg": "#08c614",
                             "insertbackground": "#08c614",
                             "selectbackground": "#f01c1c"}
        self.can0 = ScrolledText(self.top, **self.text_options)
        self.can0.place(relx=labelX, rely=1-0.5, relwidth=0.4, relheight=0.3)
        
        self.canType = 0
        self.command = ""  
        self.popen = None     # will hold a reference to a Popen object
        self.running = False  # True if the process is running

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self._tk = master

    def Command1_Cmd(self, event=None):
        print(self.text0[0].get(0.0,END))
        self.canType = 0
        self.text = self.can0
        out = self.conn.exec_command("candump can0")
        self.show(out)
        pass

    def Command2_Cmd(self, event=None):
        print(self.text1[0].get(0.0,END))
        self.canType = 0
        self.text = self.can0
        out = self.conn.exec_command("candump can0")
        self.show(out)
        pass

    def Command3_Cmd(self, event=None):
        s = self.comboData[self.Combo.current()]
        self.canType = 0
        self.text = self.can0
        if s == "内核":
            self.command = "cat /proc/version"
            out = self.conn.exec_command(self.command)
            self.show(out)
        elif s == "设备树":
            self.command = " dmesg | grep DTB"
            out = self.conn.exec_command(self.command)
            self.show(out)
        elif s == "文件系统":
            self.command = "df -T"
            out = self.conn.exec_command(self.command)
            self.show(out)
        elif s == "FPGA":
            # self.command = "spidev_test -v -D /dev/spidev1.0 -s 25000000 -p SPIR\\x05\\x00XXXXX"
            # out = self.conn.exec_command(self.command)
            # self.show(out)

            test = "RX | 08 00 00 00 00 00 F0 08 02 01 13"
            r = test.split(" ")
            r8 = r[8][0]
            self.show("硬件版本："+r[8][0]+"\n")
            self.show("硬件编号："+r[8][1]+" "+r[9]+"\n")
            self.show("软件版本号："+r[10]+" "+r[11]+" "+r[12]+"\n")

        else:
            self.command = "cat /proc/version"
            out = self.conn.exec_command(self.command)
            self.show(out)
        
        print(s)
        
        pass
    
    def Command5_Cmd(self, event=None):
        # showinfo("连接","敬请期待！")
        self.conn = SSHConnection(self.sshText[0].get(0.0,END), 22, 'titan', self.sshText[1].get(0.0,END),self)
        
        pass
    
    def Command6_Cmd(self, event=None):
        # showinfo("Exit","敬请期待！")
        self._tk.destroy()
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
