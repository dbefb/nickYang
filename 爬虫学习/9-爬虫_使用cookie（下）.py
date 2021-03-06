# 使用cookiejar完整代码
from urllib import request,parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 常见cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求的管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    # 负责首次登录，输入用户名和密码，用来获取cookie
    url = 'http://www.renren.com/PLogin.do'

    id = input('请输入用户名：')
    pw = input('请输入密码：')

    data = {
        # 从input标签的name获取参数的key，value由输入获取
        "email": id,
        "password": pw
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url,data=data.encode('utf-8'))
    # 使用opener发起请求
    rsp = opener.open(req)

# 以上代码就可以进一步获取cookie了，cookie在哪呢？cookie在opener里
def getHomePage():
    # 地址是用在浏览器登录后的个人信息页地址
    url = "http://www.renren.com/973663294/profile"

    # 如果已经执行login函数，则opener自动已经包含cookie
    rsp = opener.open(url)
    html = rsp.read().decode()

    with open("rsp1.html", "w", encoding="utf-8")as f:
        # 将爬取的页面
        print(html)
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()
