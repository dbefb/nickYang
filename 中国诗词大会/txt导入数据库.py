import jieba
import sys  
import re   
import random
from random import randrange
import os,time
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='newbegin',db='lsj',charset='utf8')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

class WordCreate():
    def __init__(self,path):
        '''
        导入文件进行解析
        '''
        with open(path,encoding="utf-8") as file:
            content = file.read()
            
            x = re.findall(r'\((.*)\)', content)
            
            for i in x:
                zifu = '('+i+')'
                content = content.replace(zifu,'')
                
            content = re.split(r'\d', content)
            content = [i for i in content if i != '']
            self.sc_list = []
            for i in content:
                weak_list = re.split(r'[、。；\n\s*]',i)
                weak_list = [i for i in weak_list if i != '']
                self.sc_list.append(weak_list)
        # print(self.sc_list)
    def OperationSql(self):
        num=1
        for i in self.sc_list:
            for _ in range(11-len(i)):
                i.append('NULL')          
            cur.execute("INSERT INTO poetry(id,name,author,sentense_1,sentense_2,\
                sentense_3,sentense_4,sentense_5,sentense_6,sentense_7,sentense_8,\
                    sentense_9,sentense_10) VALUES (%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%\
                        (num,i[0],'NULL',i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
            conn.commit()
            num+=1
def main():
    
    generator = WordCreate('D:\桌面\诗词库.txt')  #选择合适的路径
    generator.OperationSql()
    
    
if __name__ == '__main__':
    main()