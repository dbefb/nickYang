# 使用代理服务器访问猫眼
# https://maoyan.com/
#https://blog.csdn.net/qq_40147863/article/details/81738970
from urllib import request,error,parse
import json
import requests
import random
from PIL import Image
from bs4 import BeautifulSoup
def yzm(Session):
    url = 'https://www.chsi.com.cn/cet/ValidatorIMG.JPG?ID='+str(random.random()*10000)

    header = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=BE4E3DD70FF5E30CD76704D9B6428CF8; zg_did=%7B%22did%22%3A%20%22170605eeefdaf-09392db11320fc-6313f69-144000-170605eeefe232%22%7D; _ga=GA1.3.246358658.1582164799; _gid=GA1.3.1426041970.1582255137; _gat_gtag_UA_100524_1=1; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201582297207619%2C%22updated%22%3A%201582297225053%2C%22info%22%3A%201582164799252%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%7DCookie: JSESSIONID=BE4E3DD70FF5E30CD76704D9B6428CF8; zg_did=%7B%22did%22%3A%20%22170605eeefdaf-09392db11320fc-6313f69-144000-170605eeefe232%22%7D; _ga=GA1.3.246358658.1582164799; _gid=GA1.3.1426041970.1582255137; _gat_gtag_UA_100524_1=1; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201582297207619%2C%22updated%22%3A%201582297225053%2C%22info%22%3A%201582164799252%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%7D',
        'Host': 'www.chsi.com.cn',
        'Referer': 'https://www.chsi.com.cn/cet/query',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
    }
    proxies = {
        "http":"http://221.180.170.104:8080"
    # "https":"https://192.168.0.1:80"
        }
    try:
        Session.headers=header
        Session.proxies=proxies
    
        res = Session.get(url,headers=header,proxies=proxies)
        print(res.content)
        with open('D:/img.jpg', 'wb') as f:
            f.write(res.content)
        
    except Exception as e:
        print("Imgae_Error:", e.args)


def login(Session):
    
    Image.open('D:/img.jpg').show()
    yzm=input('请输入:')
    url = "https://www.chsi.com.cn/cet/query"
    header = {
                
                # Cookie值从登录后的浏览器，拷贝，方法文章上面有介绍
            
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control":"max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "60",
            "Content-Type": "application/x-www-form-urlencoded",
            
            "Host": "www.chsi.com.cn",
            "Origin": "https://www.chsi.com.cn",
            "Referer": "https://www.chsi.com.cn/cet/query",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "ame-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
                
    }
    proxies = {
        "http":"112.111.217.61:9999"
        # "https":"https://192.168.0.1:80"
    }
    
    data = {
        'zkzh': '420241192202008',
        'xm': '刘斯杰',
        'yzm':yzm
    }
                    
    try:
        res = Session.post(url,headers=header,data=data,proxies=proxies)
        str_json = res.content.decode()
        print(str_json)
        soup=BeautifulSoup(str_json,'lxml')
        data2=soup.prettify()
        name = soup.select('td[colspan="2"]')
        score = soup.select('span[class="colorRed"]')
        print('姓名:',(name[0].text).strip())
        print('分数:',(score[0].text).strip())
        res = Session.post(url,headers=header,data=data,proxies=proxies)
        str_json = res.content.decode()
        print(str_json)
        soup=BeautifulSoup(str_json,'lxml')
        data2=soup.prettify()
        name = soup.select('td[colspan="2"]')
        score = soup.select('span[class="colorRed"]')
        print('姓名:',(name[0].text).strip())
        print('分数:',(score[0].text).strip())
                        
                        # print(str_json)
                        

    except error.HTTPError as e:
        print(e)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    s=requests.Session()
    yzm(s)
    login(s)
   
