import jieba
import sys  
import re   
import random
from random import randrange
import os,time
from urllib import  request,error
from bs4 import BeautifulSoup
def Spider():
    '''
    爬取此网站小学的诗词
    '''
    url = "https://so.gushiwen.org/gushi/xiaoxue.aspx"

    try:

        req = request.Request(url)

        rsp = request.urlopen(req)

        html = rsp.read().decode()
        soup=BeautifulSoup(html,'lxml')
        html=soup.prettify()
        div = soup.find_all('a',{'target':'_blank'})
        div = div[1:-1]
        name = div[0].string
        f = open('D:\桌面\诗词库.txt','w+',encoding='utf-8')
        num = 1
        for i in div:
        #     print(i.string)
        #     print(i.get('href'))
            name = i.string
            url = i.get('href')
            req = request.Request(url)
            rsp = request.urlopen(req)
            html = rsp.read().decode()
            
            soup=BeautifulSoup(html,'lxml')
            html=soup.prettify()
            div2 = soup.find('meta',{'name':'description'})
            print(div2.get('content'))
            
            f.writelines([str(num),name,'\n',div2.get('content'),'\n'])
            f.close
            num+=1
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)


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
                print(i)
                zifu = '('+i+')'
                print(zifu)
                content = content.replace(zifu,'')
                print(content)
            print(content)
            content = re.split(r'\d', content)
            content = [i for i in content if i != '']
            self.sc_list = []
            for i in content:
                weak_list = re.split(r'[、。\n\s*]',i)
                weak_list = [i for i in weak_list if i != '']
                self.sc_list.append(weak_list)
        print(self.sc_list)
    def random_choice(self):
        '''
        对解析好的文件进行选句、选词
        '''
        whole_sentences = random.choice(self.sc_list)
        sentences_name = whole_sentences[0]
        random_sentence_index = randrange(2,len(whole_sentences))
        random_sentence = whole_sentences[random_sentence_index]
        seg_list = jieba.cut(random_sentence,cut_all=False)
        seg_list = list(seg_list)
        seg_list = [i for i in seg_list if i != '，']
        random_word = random.choice(seg_list)
        print(random_word,'\n')
        print('请按回车查看答案')
        while True:
            key = input()
            if key == '':
                print('答案为：{}:{}\n'.format(whole_sentences[0],random_sentence))
                break
            else:
                print('请输入回车')
    def loop_execution(self):
        '''
        循环执行命令
        '''
        while True:
            self.random_choice()
            print('输入1退推出游戏，按回车继续')
            key = input()
            if key == '':
                continue
            elif key == '1':
                print('欢迎再玩')
                break
            else:
                print()
            
def main():
    Spider()
    generator = WordCreate('D:\桌面\诗词库.txt')  #选择合适的路径
    generator.loop_execution()

if __name__ == '__main__':
    main()