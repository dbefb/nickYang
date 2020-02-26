# 先安装lxml
# 用 lxml 来解析HTML代码

# from lxml import etree

# text = '''
# <div>
#     <ul>
#         <li class="item-0"><a href="0.html">item 0 </a></li>
#         <li class="item-1"><a href="1.html">item 1 </a></li>
#         <li class="item-2"><a href="2.html">item 2 </a></li>
#         <li class="item-3"><a href="3.html">item 3 </a></li>
#         <li class="item-4"><a href="4.html">item 4 </a></li>
#         <li class="item-5"><a href="5.html">item 5 </a></li>
#     </ul>     
# </div>
# '''

# # 利用 etree.HTML 把字符串解析成 HTML 文件
# html = etree.HTML(text)
# s = etree.tostring(html).decode()
# # print(html)
# print(s)

# # lxml-etree读取文件
# xml = etree.parse("Package.xml")
# sxml = etree.tostring(xml, pretty_print=True)

# print(sxml)

# lxml-etree读取文件

from lxml import etree

xml = etree.parse("Package.xml")
print(type(xml))

# 查找所有 book 节点
rst = xml.xpath('//book')
print(type(rst))
print(rst)

# 查找带有 category 属性值为 sport 的元素
rst2 = xml.xpath('//book[@category="sport"]')

print(type(rst2))
print(rst2[0].text)

# 查找带有category属性值为sport的元素的book元素下到的year元素
rst3 = xml.xpath('//book[@category="sport"]/year')
rst3 = rst3[0]

print('-------------\n',type(rst3))
print(rst3.tag)
print(rst3.text)

