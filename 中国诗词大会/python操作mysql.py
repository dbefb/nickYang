import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='newbegin',db='lsj',charset='utf8')

cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
num=2
for _ in range(0,59):
    cur.execute('ALTER TABLE poetry ADD COLUMN yiwen_'+str(num)+' varchar(100) NOT NULL')
    num+=1
# cur.execute('select * from poetry')
# poetry = cur.fetchall()
# print(poetry[379])
# poetry = poetry[379]
# print(poetry['name']+'\n')
# num = 1
# for _ in range(len(poetry)):
#     print(poetry['sentense_'+str(num)])
#     if num  == 61:
#         break
#     num+=1



