# python爬虫实现百度翻译
# urllib和request POST参数提交
# 缺少包请自行查看之前的笔记
#https://www.jianshu.com/p/4c3e228940c8  这个是用到的知识
#https://blog.csdn.net/qq_40147863/article/details/81590849 这个是此代码的网站
from urllib import request,parse
import json

def fanyi(keyword):
    base_url = 'https://fanyi.baidu.com/sug'

    # 构建请求对象
    data = {
        'kw': keyword
    }
    data = parse.urlencode(data)
    print("即将发送的data数据的类型：{0}".format(type(data)))
    # 模拟浏览器
    header = {"User-Agent": "mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}

    req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=header)
    res = request.urlopen(req)

    # 获取响应的json字符串
    str_json = res.read().decode('utf-8')

    print("查看返回数据的类型：{0}".format(type(str_json)))
    # 把json转换成字典
    myjson = json.loads(str_json)

    print(myjson) #看看咱的json

    print("转换后的数据类型：{0}".format(type(myjson)))

    info = myjson['data'][0]['v']  #data中标号 第一位 的数据中 类型为'v'的数据
    print(info)

    for i in myjson["data"]:
        print(i['k'],":",i['v'])  #data中每一个标号 的数据中 类型为'k'和'v'的数据

if __name__=='__main__':
    while True:
        keyword = input('请输入翻译的单词：')
        if keyword == 'q':
            break
        fanyi(keyword)
