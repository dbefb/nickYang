import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import jieba
import sys  
import re   
import random
from random import randrange
import os,time

class WordCreate():
    def __init__(self,path):
        '''
        导入文件进行解析
        '''
        with open(path,encoding="utf-8") as file:
            content = file.read()
            
            x = re.findall(r'\((.*)\)', content)
            # content = content.replace('29','cao')
            for i in x:
                
                zifu = '('+i+')'
                
                content = content.replace(zifu,'')
                
            
            content = re.split(r'\d', content)
            content = [i for i in content if i != '']
            self.sc_list = []
            for i in content:
                weak_list = re.split(r'[、。\n\s*]',i)
                weak_list = [i for i in weak_list if i != '']
                self.sc_list.append(weak_list)
        
    def random_choice(self):
        '''
        对解析好的文件进行选句、选词
        '''
        whole_sentences = random.choice(self.sc_list)
        sentences_name = whole_sentences[0]
        random_sentence_index = randrange(1,len(whole_sentences))
        random_sentence = whole_sentences[random_sentence_index]
        seg_list = jieba.cut(random_sentence,cut_all=False)
        seg_list = list(seg_list)
        seg_list = [i for i in seg_list if i != '，']
        random_word = random.choice(seg_list)
        return random_word,sentences_name,random_sentence
       

generator = WordCreate('D:\桌面\诗词库.txt')  #选择合适的路径

window = tk.Tk()

window.title('My Window')

window.geometry('400x150') 
buttons = []
neirong = []

def des(index,n):
    window = tk.Tk()
    window.title('My Window')
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
        print(i)
        for j in range(4):
            index = j+i*4
            word,name,sentence = generator.random_choice()
            sc_list = [word, name, sentence]
            neirong.append(sc_list)
            n = neirong[index]
            c = tk.Button(window, text=word, font=('Arial', 12), width=10, height=1, command=lambda index=index,n=n:des(index,n))
            c.grid(row=i, column=j, padx=1, pady=1, ipadx=1, ipady=1)
            buttons.append(c)
            print(word)
            
b = tk.Button(window, text='进入游戏', font=('Arial', 12), width=10, height=1, command=create_key_word)
b.place(x=200, y=70, anchor='s')
window.mainloop()
