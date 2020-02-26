# py02v1.py
#https://blog.csdn.net/qq_40147863/article/details/81451202
from urllib import request
import chardet
if __name__ == '__main__':

    url = "https://xiaoyuan.zhaopin.com/company/CC000453722D90000000000"
    rsp = request.urlopen(url)
    # 按住Ctrl键不送，同时点击urlopen，可以查看文档，有函数的具体参数和使用方法

    html = rsp.read()
    # 解码
    cs = chardet.detect(html)

    print("cs的类型：{0}".format(type(cs)))
    print("监测到的cs数据：{0}".format(cs))

    html = html.decode(cs.get("encoding", "utf-8"))
    # 意思是监测到就使用监测到的，监测不到就使用utf-8

    print("HTML页面为：\n%s" % html)

    #html = html.decode()

    print(html)
