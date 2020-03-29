import pymysql
import random
import jieba
def CallMySql():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='newbegin',db='lsj',charset='utf8')

    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

    cur.execute('select * from poetry')
    poetry = cur.fetchall()

    random_poetry = random.choice(poetry)

    random_poetry = {i:random_poetry[i] for i in random_poetry if random_poetry[i]!='NULL'}

    poetry_length = len(random_poetry)
    # print(random_poetry)
    sentence = random_poetry['sentense_'+str(random.randint(1,poetry_length-2))]
    seg_sentence = jieba.cut(sentence, cut_all=False)
    seg_sentence = list(seg_sentence)
    seg_sentence = [i for i in seg_sentence if i !='，']
    key_word = random.choice(seg_sentence)
    # print(key_word,sentence)
    # print(random_poetry)
    # print('word,name,sentence:',key_word,random_poetry['name'],sentence)

    return key_word,random_poetry['name'],sentence
