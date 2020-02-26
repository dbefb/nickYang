# py04v3.py
#https://blog.csdn.net/qq_40147863/article/details/81460484
from urllib import request

if __name__ == '__main__':

    url = 'https://xiaoyuan.zhaopin.com/company/CC000453722D90000000000'

    rsp = request.urlopen(url)
    # 按住Ctrl键不送，同时点击urlopen，可以查看文档，有函数的具体参数和使用方法

    print("rsp的类型：{0}".format(type(rsp)))
    print("rsp的内容：{0}".format(rsp))
    print("url为：{0}".format(rsp.geturl()))
    print("Info为：{0}".format(rsp.info())) #info：请求返回对象的meta信息
    print("Code为：{0}".format(rsp.getcode())) #getcode：返回的http code


    html = rsp.read()
