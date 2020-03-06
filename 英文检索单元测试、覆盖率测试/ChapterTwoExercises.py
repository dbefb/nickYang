"""实现对英文文档的分词分句，给出所查单词位置"""
import sys  

import re       

from memory_profiler import profile

class TxtHandle:
    """txt文档的分析"""
    def __init__(self, contents_path, query_path):
        '''
        导入待分析文件
        '''
        if not isinstance(contents_path, str):
            raise TypeError("contents_path should be str")
        if not isinstance(query_path, str):
            raise TypeError("query_path should be str")
        with open(contents_path, encoding="utf-8") as file:
            self.content = file.read()
            self.content = (self.content).lower()
            self.content = (self.content).replace('\n', ' ')
            self.content = re.split(r'[.!?]', self.content)
            del self.content[-1]        #删除最后一个元素，最后一句是句子删除的就是空元素，不是句子删除的就是不完整的句子
            self.content = [i for i in self.content if i != '']
            self.query_file(query_path)

    def query_file(self, path):
        '''
        导入查询文件，把里面的单词弄成一个列表1
        '''
        with open(path, encoding="utf-8") as file:
            self.query = (file.read()).lower()
            self.query = (self.query).split('\n')
            self.query = [i for i in self.query if i != '']

    def file_analysis(self):
        '''
        对两个文档进行处理，调用findSubscript进行单词在句子、句子在列表中的位置定位
        '''
        position_list = []
        for word in self.query:
            for sentences in self.content:
                if sentences.find(word) != -1:
                    setences_position = (self.content).index(sentences)
                    sentences = re.split(r'[ +\'\’\,]', sentences)
                    sentences = [i for i in sentences if i != '']   #删除列表空元素
                    word_position = [i for i, x in enumerate(sentences) if x == word]
                    if word_position is None:
                        pass
                    else:
                        for i in word_position:
                            position_list.append(str(setences_position+1)+'/'+str(i+1))

            if position_list == []:
                print('None')
            else:
                print(','.join(position_list))
                position_list = []

@profile
def main():
    '''
    sys.argv[1]为待分析文件
    sys.argv[2]为查询文件
    '''
    # txt = TxtHandle(sys.argv[1], sys.argv[2])
    txt = TxtHandle('D:\桌面\eng2.txt', 'D:\桌面\query.txt')
    txt.file_analysis()

if __name__ == '__main__':

    main()
