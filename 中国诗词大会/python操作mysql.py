import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='newbegin',db='lsj',charset='utf8')

cur = conn.cursor(cursor=pymysql.cursors.DictCursor)


cur.execute("INSERT INTO fucku(id,name,score)VALUES('%s','%s','%s')"%('4','李四','的'))

conn.commit()        
result = cur.fetchall()

print(result)
