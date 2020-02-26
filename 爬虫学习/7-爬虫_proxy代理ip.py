# 使用代理服务器访问猫眼
# https://maoyan.com/
#https://blog.csdn.net/qq_40147863/article/details/81738970
from urllib import request,error

if __name__ == '__main__':

    url = "https://movie.douban.com"
    header = {
            
            # Cookie值从登录后的浏览器，拷贝，方法文章上面有介绍
        
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
           
        }
    
    # 1.设置代理地址
    proxy = {'http': '121.40.119.149:3128'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)

    # 下面再进行访问url就会使用代理服务器
    try:
        req=request.Request(url=url,headers=header)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        with open("rsp.html","w",encoding="utf-8")as f:
            # 将爬取的页面
            print(html)

            f.write(html)
        

    except error.HTTPError as e:
        print(e)

    except Exception as e:
        print(e)
