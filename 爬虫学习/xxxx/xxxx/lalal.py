import requests

url = "http://www.baidu.com/"
proxies = {"http": "http://210.26.49.88:3128"}
#空白位置为测试代理ip和代理ip使用端口

headers = {"User-Agent": "Mozilla/5.0"}
#响应头
res = requests.get(url, proxies=proxies, headers=headers)
#发起请求
print(res.status_code) #返回响应码
