import re
import random

def __init__(path):
        
        with open (path) as f:
            query = f.read()
            
            query = re.split(r'[ .!?="±,°;\n\[\]\(\)]',query)
            query = [ i for i in query if i!= '']
            with open ('D:\桌面\query.txt','w') as tf:
                for i in range(1,1001):
                    tf.write(query[random.randint(0,10000)])
                    tf.write('\n')
__init__('D:\桌面\eng.txt')