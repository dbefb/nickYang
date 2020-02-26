# -*- coding: utf-8 -*-
import scrapy
import json
from urllib import request,error
from bs4 import BeautifulSoup
from xxxx.items import juQingItem,xiJuItem,dongZuoItem,aiQingItem,keHuanItem,dongHuaItem,xuanYiItem,jinSongItem,kongBuItem,jiLuItem,duanPianItem,qingSeItem,tongXingItem,yinYueItem,geWuItem,jiaTingItem,erTongItem,zhuanJiItem,liShiItem,zhanZhenItem,fanZuiItem,xiBuItem,qiHuanItem,maoXianItem,zaiNanItem,wuXiaItem,guZhuangItem,yunDongItem,heiSeItem
class SpiderCsdnSpider(scrapy.Spider):


    name = 'spider_csdn'
    allowed_domains = ['movie.douban.com']
    start_urls = [
        'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1000',#剧情
        'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=1000',#喜剧
        'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=1000',#动作
        'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=1000',#爱情
        'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=1000',#科幻
        'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=1000',#动画
        'https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=0&limit=1000',#悬疑
        'https://movie.douban.com/j/chart/top_list?type=19&interval_id=100%3A90&action=&start=0&limit=1000',#惊悚
        'https://movie.douban.com/j/chart/top_list?type=20&interval_id=100%3A90&action=&start=0&limit=1000',#恐怖
        'https://movie.douban.com/j/chart/top_list?type=1&interval_id=100%3A90&action=&start=0&limit=1000',#记录
        'https://movie.douban.com/j/chart/top_list?type=23&interval_id=100%3A90&action=&start=0&limit=1000',#短片
        'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&start=0&limit=1000',#情色
        'https://movie.douban.com/j/chart/top_list?type=26&interval_id=100%3A90&action=&start=0&limit=1000',#同性
        'https://movie.douban.com/j/chart/top_list?type=14&interval_id=100%3A90&action=&start=0&limit=1000',#音乐
        'https://movie.douban.com/j/chart/top_list?type=7&interval_id=100%3A90&action=&start=0&limit=1000',#歌舞
        'https://movie.douban.com/j/chart/top_list?type=28&interval_id=100%3A90&action=&start=0&limit=1000',#家庭
        'https://movie.douban.com/j/chart/top_list?type=8&interval_id=100%3A90&action=&start=0&limit=1000',#儿童
        'https://movie.douban.com/j/chart/top_list?type=2&interval_id=100%3A90&action=&start=0&limit=1000',#传记
        'https://movie.douban.com/j/chart/top_list?type=4&interval_id=100%3A90&action=&start=0&limit=1000',#历史
        'https://movie.douban.com/j/chart/top_list?type=22&interval_id=100%3A90&action=&start=0&limit=1000',#战争
        'https://movie.douban.com/j/chart/top_list?type=3&interval_id=100%3A90&action=&start=0&limit=1000',#犯罪
        'https://movie.douban.com/j/chart/top_list?type=27&interval_id=100%3A90&action=&start=0&limit=1000',#西部
        'https://movie.douban.com/j/chart/top_list?type=16&interval_id=100%3A90&action=&start=0&limit=1000',#奇幻
        'https://movie.douban.com/j/chart/top_list?type=15&interval_id=100%3A90&action=&start=0&limit=1000',#冒险
        'https://movie.douban.com/j/chart/top_list?type=12&interval_id=100%3A90&action=&start=0&limit=1000',#灾难
        'https://movie.douban.com/j/chart/top_list?type=29&interval_id=100%3A90&action=&start=0&limit=1000',#武侠
        'https://movie.douban.com/j/chart/top_list?type=30&interval_id=100%3A90&action=&start=0&limit=1000',#古装
        'https://movie.douban.com/j/chart/top_list?type=18&interval_id=100%3A90&action=&start=0&limit=1000',#运动
        'https://movie.douban.com/j/chart/top_list?type=31&interval_id=100%3A90&action=&start=0&limit=1000'#黑色
    ]
    
    def parse(self, response):
        # print(response.body)
        data=json.loads(response.body)
        header = {
            
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

        if response.url == self.start_urls[0]:
            item=juQingItem()
            print('正在爬取剧情电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[1]:
            item=xiJuItem()
            print('正在爬取喜剧电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[2]:
            item=dongZuoItem()
            print('正在爬取动作电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[3]:
            item=aiQingItem()
            print('正在爬取爱情电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[4]:
            item=keHuanItem()
            print('正在爬取科幻电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[5]:
            item=dongHuaItem()
            print('正在爬取动画电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[6]:
            item=xuanYiItem()
            print('正在爬取悬疑电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                           
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[7]:
            item=jinSongItem()
            print('正在爬取惊悚电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[8]:
            item=kongBuItem()
            print('正在爬取恐怖电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[9]:
            item=jiLuItem()
            print('正在爬取记录电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[10]:
            item=duanPianItem()
            print('正在爬取短片电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[11]:
            item=qingSeItem()
            print('正在爬取情色电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[12]:
            item=tongXingItem()
            print('正在爬取同性电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[13]:
            item=yinYueItem()
            print('正在爬取音乐电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[14]:
            item=geWuItem()
            print('正在爬取歌舞电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[15]:
            item=jiaTingItem()
            print('正在爬取家庭电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[16]:
            item=erTongItem()
            print('正在爬取儿童电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[17]:
            item=zhuanJiItem()
            print('正在爬取传记电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                           
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[18]:
            item=liShiItem()
            print('正在爬取历史电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[19]:
            item=zhanZhenItem()
            print('正在爬取战争电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[20]:
            item=fanZuiItem()
            print('正在爬取犯罪电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[21]:
            item=xiBuItem()
            print('正在爬取西部电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[22]:
            item=qiHuanItem()
            print('正在爬取奇幻电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                           
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[23]:
            item=maoXianItem()
            print('正在爬取冒险电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[24]:
            item=zaiNanItem()
            print('正在爬取灾难电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                           
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[25]:
            item=wuXiaItem()
            print('正在爬取武侠电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[26]:
            item=guZhuangItem()
            print('正在爬取古装电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[27]:
            item=yunDongItem()
            print('正在爬取运动电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item
        if response.url == self.start_urls[28]:
            item=heiSeItem()
            print('正在爬取黑色电影排行榜...')
            for i in data:
                item['filmName'] = i['title']
                item['scores'] = i['score']
                item['rank'] = i['rank']
                try:
                    req=request.Request(url=i['url'],headers=header)
                    rsp=request.urlopen(req)
                    data2=rsp.read()
                    
                    soup=BeautifulSoup(data2,'lxml')
                    data2=soup.prettify()
                    div = soup.select("a[class='playBtn']")
                    
                    t=0
                    if div == []:
                        item['href']='无连接'
                    else:
                        for x in div:
                            
                            t+=1
                            item['weishu']=str(t)
                        item['href']=div[0]['href']
                        for x in range(1,t):
                            item['href'+str(x+1)]=div[x]['href']
                except error.HTTPError as e:
                    print(e)
                    
                except Exception as e:
                    print(e)
                    
                yield item