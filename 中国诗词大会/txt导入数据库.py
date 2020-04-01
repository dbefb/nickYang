import sys  
import re  
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
            
            x = re.findall(r'[（|(](.*?)[）|)]', content)
            print(x)
            for i in x:
                zifu = '('+i+')'
                content = content.replace(zifu,'')
                
            content = re.split(r'\d', content)
            content = [i for i in content if i != '']
            self.sc_list = []
            for i in content:
                weak_list = re.split(r'[、。；！？\n\s*]',i)
                weak_list = [i for i in weak_list if i != '']
                self.sc_list.append(weak_list)
        # print(self.sc_list)
    def OperationSql(self):
        num=130
        for i in self.sc_list:
            for _ in range(62-len(i)):
                i.append('NULL')
                print(len(i))
            cur.execute("INSERT INTO poetry(id,name,author,sentense_1,sentense_2,\
                sentense_3,sentense_4,sentense_5,sentense_6,sentense_7,sentense_8,\
                    sentense_9,sentense_10,sentense_11,sentense_12,\
                sentense_13,sentense_14,sentense_15,sentense_16,sentense_17,sentense_18,\
                    sentense_19,sentense_20,sentense_21,sentense_22,\
                sentense_23,sentense_24,sentense_25,sentense_26,sentense_27,sentense_28,\
                    sentense_29,sentense_30,sentense_31,sentense_32,\
                sentense_33,sentense_34,sentense_35,sentense_36,sentense_37,sentense_38,\
                    sentense_39,sentense_40,sentense_41,sentense_42,\
                sentense_43,sentense_44,sentense_45,sentense_46,sentense_47,sentense_48,\
                    sentense_49,sentense_50,sentense_51,sentense_52,\
                sentense_53,sentense_54,sentense_55,sentense_56,sentense_57,sentense_58,\
                    sentense_59,sentense_60,sentense_61) VALUES (%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'\
                        ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'\
                            ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'\
                                ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'\
                                    ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'\
                                        )"%\
                        (num,i[0],'NULL',i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]\
                            ,i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20]\
                            ,i[21],i[22],i[23],i[24],i[25],i[26],i[27],i[28],i[29],i[30]\
                            ,i[31],i[32],i[33],i[34],i[35],i[36],i[37],i[38],i[39],i[40]\
                            ,i[41],i[42],i[43],i[44],i[45],i[46],i[47],i[48],i[49],i[50]\
                            ,i[51],i[52],i[53],i[54],i[55],i[56],i[57],i[58],i[59],i[60],i[61]))
            conn.commit()
            num+=1
def main():
    
    generator = WordCreate('D:\桌面\诗词库2.txt')  #选择合适的路径
    generator.OperationSql()
    
    
if __name__ == '__main__':
    main()