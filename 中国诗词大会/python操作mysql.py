import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='newbegin',db='lsj',charset='utf8')

cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

cur.execute('SELECT * FROM poetry')

result = cur.fetchall()

print(result[1]['name'])