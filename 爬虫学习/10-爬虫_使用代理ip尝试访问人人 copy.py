from urllib import request,error

if __name__ == '__main__':
   
    url = "http://www.renren.com/973663294/profile"
    header = {
        
        # Cookie值从登录后的浏览器，拷贝，方法文章上面有介绍
        "Cookie": "anonymid=k6edc8jvn2xrx2; depovince=HAN; _r01_=1; JSESSIONID=abcSbwucL0I1P8cQJONax; ick_login=0a8c853a-32bb-4d9b-a907-4b1dbae1cc16; taihe_bi_sdk_uid=5427a15a419a5832f7c1bfaec634c4bb; taihe_bi_sdk_session=3ea0d5a2ad917883bc37058f93780e3e; first_login_flag=1; ln_uact=1160132795@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=94b93b4c-6cdb-4d0d-9061-50e2d1ee96b8%7C0820d5c9ef6f61ebd5160824c97ecb4f%7C1581213435840%7C1%7C1581213435917; jebe_key=94b93b4c-6cdb-4d0d-9061-50e2d1ee96b8%7C0820d5c9ef6f61ebd5160824c97ecb4f%7C1581213435840%7C1%7C1581213435921; wp_fold=0; jebecookies=4219fa75-0033-4247-a697-a561b5772470|||||; _de=6733C3755B7E63E1A8B2B489079C1CFE6DEBB8C2103DE356; p=7a6d577a92c196ef59f97042a732d3b44; t=be19b869b7f27dd32be3fa8f09fc13074; societyguester=be19b869b7f27dd32be3fa8f09fc13074; id=973663294; xnsid=d8387c1b; ver=7.0; loginfrom=null",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
   
    # 1.设置代理地址
    proxy = {'http': '119.23.79.199:3128'}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)
    try:

        req = request.Request(url=url,headers=header)
      
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