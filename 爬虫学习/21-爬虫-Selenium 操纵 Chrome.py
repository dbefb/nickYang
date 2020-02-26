# Selenium + Chrome 案例1
from selenium import webdriver

# 路径是自己解压安装 Chromedriver 的路径
driver = webdriver.Chrome()

url = "https://www.chsi.com.cn/cet/query"

driver.get(url)

# 根据id查找，后面加.text 表示拿看到的文本数据
text = driver.text
print(text)
