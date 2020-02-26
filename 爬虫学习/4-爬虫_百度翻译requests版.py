# 百度翻译
# 添加包的方法在上面
#https://blog.csdn.net/qq_40147863/article/details/81591145
import requests
import json

def fanyi(keyword):
    url = 'https://fanyi.baidu.com/sug'
    
    # 定义请求参数
    data = {
        
        'kw': keyword
    }

    # 发送请求，抓取信息
    res = requests.post(url,data=data)

    # 解析结果并输出
    str_json = res.text

    myjson = json.loads(str_json)
    
    info = myjson['data'][0]['v']
    print(info)
    for i in myjson['data']:
        print(i['k'],':',i['v'])
if __name__=='__main__':
    while True:
        keyword = input('请输入翻译的单词：')
        if keyword == 'q':
            break
        fanyi(keyword)
