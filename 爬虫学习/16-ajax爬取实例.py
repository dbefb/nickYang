# 爬取豆瓣电影数据
# 了解ajax的爬取方式
# https://movie.douban.com/
# https://blog.csdn.net/qq_40147863/article/details/82079839

from urllib import request,error
import json
from bs4 import BeautifulSoup
# url信息：interval_id表示排名段（可自行修改），limit限制20个
if __name__ == '__main__':

    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"

    header = {
            
            # Cookie值从登录后的浏览器，拷贝，方法文章上面有介绍
        
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
           
        }
    
    # 1.设置代理地址
    proxy = {'http': '210.26.49.88:3128'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)
    try:
        # req=request.Request(url=url,headers=header)
        # rsp=request.urlopen(req)
        # data2=rsp.read()
        # soup=BeautifulSoup(data2,'lxml')
        # data2=soup.prettify()
        # div = soup.select("a[class='playBtn']")
        # for i in div:
        #     print(i['href'])
        req=request.Request(url=url,headers=header)
        rsp = request.urlopen(req)
        
        data = rsp.read().decode()
        print(data)
        data = json.loads(data)
        print(data)
        # # print(data['subjects'][0]['title'],data['subjects'][0]['title'],data['subjects'][0]['rate'])
        # f=open('F:/multisim/VsCode/爬虫/豆瓣电影排行榜/豆瓣最近热门电影排行榜.txt','w')
        # # for i in data:
        # #     print(i['title']," ","评分:",i['score']," ","排名:",i['rank'])
            
        # #     f.writelines([i['title'],' ','评分:',i['score'],' ','排名:',str(i['rank']),'\n'])
        # x=0
        # for i in data['subjects']:
        #     print(i['title']," ","评分:",i['rate'])
        #     x+=1
        #     f.writelines([i['title'],' ','评分:',i['rate'],'  ',str(x),'\n'])
        # f.close
    except error.HTTPError as e:
        print(e)

    except Exception as e:
        print(e)