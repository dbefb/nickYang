import sys
import re
class txtHandle(object):
    def __init__(self,path):
        '''
        导入待分析文件
        '''
        with open(path) as f:
            self.content = f.read()
            self.content = re.split(r'[.!?]',self.content)
            if self.content != '':      #如果最后一个是''，说明倒数第一句不完整，删除
                del self.content[-1]
            
    def queryFile(self,path):
        '''
        导入查询文件，把里面的单词弄成一个列表1
        '''
        with open(path) as f:
            self.query = (f.read()).split('\n')
            
                    
    def fileAnalysis(self):
        '''
        对两个文档进行处理，调用findSubscript进行单词在句子、句子在列表中的位置定位
        '''
        list=[]
        for word in self.query:
            for sentences in self.content:
    
                if sentences.find(word) != -1:

                    sentences_str = sentences
                    sentences = sentences.split(' ')
                    sentences = [i for i in sentences if i!='']   #删除列表空元素

                    setences_position = self.findSubscript(self.content,sentences_str)
                    word_position = self.findSubscript(sentences,word)

                    list.append(str(setences_position)+'/'+str(word_position))
                    
            if list == []:
                print('None')
            else:
                print(','.join(list))
                list=[]
        
    def findSubscript(self,list,element):
        '''
        查找单词在列表中的下标
        返回单词句子的位置
        '''
        for i in range(0,len(list)):

            if list[i] == element:

                return i+1
            


    
# def main():
    '''
    sys.argv[1]为待分析文件
    sys.argv[2]为查询文件
    '''
if __name__ == '__main__':
    txt = txtHandle('D:\桌面\eng.txt')
    txt.queryFile('D:\桌面\query.txt')
    txt.fileAnalysis()
    
    

