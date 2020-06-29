# -*- coding: utf-8 -*-
__author__ = 'quqiao'
"""
tkinter: python的标准tk GUI工具包接口,Unix，windows,mac系统都可以使用

tkinter组件：
            Button:
            Canvas:用来绘图，将图形，文本，小部件或框架放置在画布上
            Checkbutton:
            Entry:
            listbox:列表控件

"""

"""主框架"""
# import tkinter
# top = tkinter.Tk()
# top.mainloop()  # 进入消息循环


"""各组件使用"""
import tkinter    # 导入tkinter库
import tkinter.messagebox
root = tkinter.Tk()  # 创建窗口对象的背景色
"""listbox创建"""
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb1 = tkinter.Listbox(root)
listb2 = tkinter.Listbox(root)
for item in li:
    listb1.insert(0, item)
for item in movie:
    listb2.insert(0, item)

"""button创建"""
def helloCallBack():
    tkinter.messagebox.showinfo("hello python", "你好啊！")
B = tkinter.Button(root, text="点我", command = helloCallBack)

"""canvas创建"""
cv1 = tkinter.Canvas(root, bg="red")
cv1.create_rectangle(10, 20, 30, 40)

"""checkBox创建"""
cb1 = tkinter.Checkbutton(root, text='test01', variable=0, onvalue=1, offvalue=0, height=2, width=5)
cb2 = tkinter.Checkbutton(root, text='test02', variable=0, onvalue=1, offvalue=0, height=2, width=5)

"""label创建"""
l1 = tkinter.Label(root, text='姓名')

"""Entry创建"""
E1 = tkinter.Entry(root, bd=5)

l1.pack(side='left')
E1.pack(side='right')
cb1.pack()
cb2.pack()
cv1.pack()
B.pack()
listb1.pack()
listb2.pack()
root.mainloop()