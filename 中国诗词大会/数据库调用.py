import pymysql
import random
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='newbegin',db='lsj',charset='utf8')

cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

cur.execute('select * from poetry')
poetry = cur.fetchall()

random_poetry = random.choice(poetry)

random_poetry = {i:random_poetry[i] for i in random_poetry if random_poetry[i]!='NULL'}

poetry_length = len(random_poetry)

print('{}中的一句话:{}'.format(random_poetry['name'],random_poetry['sentense_'+str(random.randint(1,poetry_length-2))]))