# var r = function(e) {
#         var t = n.md5(navigator.appVersion),
#         r = "" + (new Date).getTime(),
#         i = r + parseInt(10 * Math.random(), 10);
#         return {
#             ts: r,
#             bv: t,
#             salt: i,
#             sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
#         }
#     };
import hashlib
import random
from urllib import request,parse
import time
from io import BytesIO
import gzip
import json

def generate_Sign_Salt(word):

    appVersion="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    bv=hashlib.md5(appVersion.encode(encoding='UTF-8')).hexdigest()
    ts=int(time.time()*1000)
    salt=ts+random.randint(0,10)
    sign=hashlib.md5(("fanyideskweb"+word+str(salt)+"n%A-rKaT5fb[Gy?;N5@Tj").encode(encoding='UTF-8')).hexdigest()

    return bv,ts,salt,sign

def translate(keyword):
    bv,ts,salt,sign = generate_Sign_Salt(keyword)
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        "i": keyword,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1342758781@10.168.1.241; OUTFOX_SEARCH_USER_ID_NCOO=622758303.0378263; JSESSIONID=aaaAJi1_BHV509hz49Xax; ___rl__test__cookies=1581386278701",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    
    req=request.Request(url=url,data=data,headers=headers)
    rsp=request.urlopen(req)
    html=rsp.read()
    buff = BytesIO(html)
    f = gzip.GzipFile(fileobj=buff)
    html = f.read().decode('utf-8')
    myjson = json.loads(html)
    print(myjson['translateResult'][0][0]['src'],":",myjson['translateResult'][0][0]['tgt'])
    print(myjson['smartResult']['entries'][1])
    print(myjson['smartResult']['entries'][2])
    print(myjson['smartResult']['entries'][3])
    

if __name__ == '__main__':
    keyword=input('请输入单词：')
    translate(keyword)