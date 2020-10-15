# python_gui
python tkinter gui demo
![](https://docimg2.docs.qq.com/image/7Fcj5fiBHJTqebO8TH3vOw)
![](https://docimg1.docs.qq.com/image/7QgKgTjEKhxouogplQvb0A)
![](https://docimg9.docs.qq.com/image/P4sEHeyRD5oq3Z2Z3kkprg)
### 使用方式  
python python_gui.py

### 文档
本程序用的是python 3.7，用anaconda管理。  

1.启动python环境。  
1.1 启动Anaconda，点击Environments，默认有个base(root)，可以自己创建一个，也可以使用默认的，点击▶。  
![](https://docimg8.docs.qq.com/image/TFHF31Fp3jpSz2AyEKkdww)
1.2 会出现一个下来菜单，点击第一个Open Terminal。  
![](https://docimg5.docs.qq.com/image/Sq3sYwDcQM6Y80YguHy78A)
1.3 出现一个终端，注意该路径，默认前面会有个(base)，代表着目前使用的是python 虚拟环境。  
![](https://docimg2.docs.qq.com/image/JfRN9YLohJ4lfHRwPcn1UA)
1.4 作为对比，从别的地方打开的终端不会带(base)。  
![](https://docimg5.docs.qq.com/image/C53DtCkOs87BkSLF2qUrVg)
1.5 python虚拟环境是一个沙盒，每个环境里安装的第三方库都是独立的，不会污染其它环境，保证每个项目的环境都是干净的，减少无用的库干扰。  

2.python_can.py说明。  
2.1 用自己喜欢的ide打开python_can.y文件。  
![](https://docimg10.docs.qq.com/image/IxPBe8henVKZou0mCPwfrw)
2.2 注意开头2行，这是固定格式，第1行的内容必须放第一行，表示本程序需要使用python运行，第2行表示本程序使用utf-8编码，不添加可能会导致程序显示中文的时候乱码。  
2.3 import导入库，程序中使用的第三方库，都需要在使用之前导入。  
![](https://docimg5.docs.qq.com/image/hYCZfAekNE6_JXwIGyxM2g)
2.4 一般情况下，需要什么功能，才会考虑导入什么库，库分为系统库和第三方库，例如os,sys,threading,tkinter，是python自带的，只要安装了python，就能使用，每个库有自己的功能，导入合适的库，能减少开发工作。  
2.5 需要注意的是，一个库导入进来，可以用也可以不用。  
2.6 导入库的两种常见方式，一种是import os，最常用的。第二种则是from [库名] import [模块]。每个库里面的功能或多或少，比如一个库里有10个功能模块，但是这个程序只用到了1个功能模块，直接import会导入很多用不到的代码。具体要不要使用看个人习惯。  
2.7 ```import tkinter as tk```，在别的地方可以能会见到这种形式的import，同样是import，但有的人可能会用自己喜欢的变量名代替库名。  
![](https://docimg5.docs.qq.com/image/HPND_s-TVnnmz9-EN5-m2w)
2.8 不同的导入方式造成的影响，用tkinter第三方库举例，Tk()是tkinter内部的初始化方法。  
| 导入 | 使用 |
| :----:| :----: |
| import tkinter | top = tkinter.Tk()     |
| import tkinter | as tk	top = tk.Tk() |  
| from tkinter   | import *	top = Tk()    |  

不同的导入方式更多的是个人习惯，对程序本身没有影响。  
2.9 第三方库paramiko，第三方库即系统不自带的，有某个人自己写好的功能分享出来，供其它人使用的，使用之前，需要用```pip install paramiko```将库下载到本地，才能在程序中导入。  

3 py文件的基本结构。  
3.1 一个py文件想要运行，至少包含导入库和程序入口。  
3.2 假如一个py文件写好后，运行的时候，首先会检查import，是否导入库，如果有就将库导入，然后找到入口，如果没有入口，该文件将什么都不做。  
3.3 找到入口后，会执行入口方法。   
3.4 ```top = Tk()```，初始化tkinter。  
3.5 ```Application(top)```将初始化完成的窗口作为参数传给用到的地方，mainloop() 启动循环，不关闭窗口的情况下，窗口将一直更新。  
![](https://docimg7.docs.qq.com/image/3Z-2F-aOo6Un2JDeKdnhiQ)
4 运行步骤。  
4.1 在终端输入```python python_can.py```文件后，首先会执行入口方法  
![](https://docimg10.docs.qq.com/image/hiisd4MqGD50fRQCuQh55A)
4.2 第311行接着会走到第120行。  
![](https://docimg3.docs.qq.com/image/7yCRKd31QkU2L_CeOs0jnQ)
4.3 第120行会走到第30行，第30行到第44行，设置了窗口的大小，标题，位置。  
4.4 第30行会一行一行的往下执行，到第45行。  
![](https://docimg4.docs.qq.com/image/AUEF5TpB6xahAi-g2WIS-g)
4.5 第45行会走到第48行，从第48行走到第116行，程序执行完毕。如果不做任何操作，程序将不会做任何事。  
![](https://docimg5.docs.qq.com/image/Dfxqz_W-Jz_GK4GmDTx4tA)
5.类，方法，数据类型，赋值，循环。  
5.1 类的作用，什么是类，为什么需要类。比如有个班级，班级里有40个学生，现在需要记录这40个学生的姓名，性别，年龄，身高，体重。  
```
张三，男，18，173cm，60kg   
李四，女，19，160cm，50kg  
...
```
当你幸幸苦苦收集完了40个学生，每个学生的5条数据。想存起来。方便以后使用，就需要一个变量来保存数据。  
```
name1 = 张三,sex1 = 男,age1=18,height1=173,weight1=60  
name2 = 李四,sex2 = 女,age2=19,height2=160,weight2=50  
...
```
为什么需要变量？因为单独一个数字，比如50，50可能是年龄，可能是体重，也可能是语文成绩，并且40个人中不止一个人有50这个数据，你不知道这个50是属于谁的。所以需要一个变量来记录，一看weight2就知道这个是体重，并且是李四的体重。  
过了几天，语文考试了，现在又需要记录每个人的语文成绩。  
于是有在每条数据后面添加一个新的变量，```yuwen1 = 60，yuwen2 = 50```。  
过了几天，又考了数学，后面还有历史，化学，生物等等。  
你开始想省点事，思考这些数据有没有办法简化，首先发现它们的相同点就是每个人的数据种类是一样的，即每个人都有行吗，性别，年龄等等。于是你就想我能不能设计一张表，包含了姓名，性别，年龄等，如果以后需要加数学成绩，历史成绩，只需要改这个表就行。每个人都是用这个表。  
这张表对应电脑里就是数据结构，一个居有相同类型数据的结构，简单点的是[]集合，里面只能放同一种数据，复杂点的就是类，能同时包含数字，字符串，还可以包含“方法”。  
```
class Student():  
    name #字符串  
    sex #字符串  
    age #数字  
stu1 = Student()
stu1.name = "张三"
stu2 = Student()
stu2.name = "李四"
```
姓名只能是字符串，不能是数字，年龄是数字而不是abc。字符串和数字就是基础数据类型。基础数据类型是计算机里保存的最基本的数据结构。复杂的数据结构是有基础数据类型组合而来。
当你把所有学生的数据全都保存成功后，现在有人叫你把他们的信息都列出来。
于是你用
```
print(stu1.name+stu1.sex+stu1.age+"")
print(stu2.name+stu2.sex+stu2.age+"")
...
```
写了很多遍之后，你发现这样的格式好像不够优雅，于是换成了
```
print("%s%s%s%s" % (stu1.name,stu1.sex,stu1.age,...))
print("%s%s%s%s" % (stu2.name,stu2.sex,stu2.age,...))
...
```
又写了很多遍，你就想这些几乎都是一样，都没有办法优化呢？于是你找到了一个叫集合和循环的东西
```
students = [stu1,stu2,stu3...]
for stu in students:
    print("%s%s%s%s" % (stu.name,stu.sex,stu.age,...))
```
然后你又想到，既然我要把每个学生的资料拼接后才显示，能不能让他们自己拼接出来，我直接显示呢？
于是有了
```
class Student():
    name #字符串
    sex #字符串
    age #数字
    def say():
        pprint("%s%s%s%s" % (name,sex,age,...))
for stu in students:
    stu.say()
```
5.2 当我们需要一个类时，需要先定义一个类，```class Student```。当我们需要一个方法时，先定义一个方法```def say()```。当我们需要一个变量时，先定义一个变量```name```，然后给它赋值```name = "张三```"
