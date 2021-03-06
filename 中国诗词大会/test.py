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
                weak_list = re.split(r'[、。？\n\s*]',i)
                weak_list = [i for i in weak_list if i != '']
                self.sc_list.append(weak_list)
        
    def random_choice(self):
        '''
        对解析好的文件进行选句、选词
        '''
        whole_sentences = random.choice(self.sc_list)
        sentences_name = whole_sentences[0]
        print(whole_sentences)
        random_sentence_index = randrange(1,len(whole_sentences))
        random_sentence = whole_sentences[random_sentence_index]
        seg_list = jieba.cut(random_sentence,cut_all=False)
        seg_list = list(seg_list)
        seg_list = [i for i in seg_list if i != '，']
        random_word = random.choice(seg_list)
        return random_word,sentences_name,random_sentence
generator = WordCreate('D:\桌面\诗词库.txt')  #选择合适的路径
for i in range(3):
        
    for j in range(4):
        word,name,sentence = generator.random_choice()
        print(word)