#案例v9
# URLError的使用
#https://blog.csdn.net/qq_40147863/article/details/81708910
from urllib import  request,error


if __name__ == '__main__':

    url = "http://www.baiiidu.com/"

    try:

        req = request.Request(url)

        rsp = request.urlopen(req)

        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
       

    except Exception as e:
        print(e)
