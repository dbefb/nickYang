import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox

import sys  
import re   
import random
from random import randrange
import os,time
import 数据库调用

window = tk.Tk()

window.title('出口成诗')

window.geometry('400x150') 
buttons = []
neirong = []

def des(index,n):
    window = tk.Tk()
    window.title('出口成诗')
    window.geometry('500x150')
    var=n[0]
    word_display = tk.Label(window, text=var, bg='green', fg='white', font=('Arial', 12), width=60, height=2)
    word_display.place(x=250,y=75,anchor='s')
    answer_button = tk.Button(window,text='点击查看答案', font=('Arial', 12), width=10, height=1, command=lambda :word_display.config(text='来自《'+n[1]+'》的：'+n[2]))
    answer_button.place(x=250,y=120,anchor='s')

def create_key_word():
    b.destroy()
    buttons = []
    neirong = []
    refresh_button = tk.Button(window, text='换一批', font=('Arial', 12), width=10, height=1, command=create_key_word)
    refresh_button.place(x=200,y=140,anchor='s')
    for i in range(3):
        
        for j in range(4):
            index = j+i*4
            word,name,sentence =  数据库调用.CallMySql()#这里用方法给word name sentence赋值即可
            sc_list = [word, name, sentence]
            neirong.append(sc_list)
            n = neirong[index]
            c = tk.Button(window, text=word, font=('Arial', 12), width=10, height=1, command=lambda index=index,n=n:des(index,n))
            c.grid(row=i, column=j, padx=1, pady=1, ipadx=1, ipady=1)
            buttons.append(c)
            
            
b = tk.Button(window, text='进入游戏', font=('Arial', 12), width=10, height=1, command=create_key_word)
b.place(x=200, y=70, anchor='s')
window.mainloop()
