import re

# 查找数字
p = re.compile(('\d+'))     # 仅匹配数字

m = p.match("one12twothree21334four2123")       # 从位置0开始匹配,不符合则返回None
m1 = p.match("one12twothree21334four2123", 3, 10)   # 从位置3开始匹配,只返回第一个匹配的结果
f = p.findall("one12twothree21334four2123")     # 匹配所有
s = p.search("one12twothree21334four2123")      # 匹配第一次出现的结果
print(m)
print(m1)
print(m1[0])    # m1是一个列表
print(f)
print(s)

# sub替换
p1 = re.compile('(\w+) (\w+)')  # 匹配两组以空格连接的字符,包括字母和数字
s1 = "hello 123 wang 456 xiaojing, i love you"
rst = p1.sub('hi 666', s1)       # 用另外两组字符替换匹配到的字符
print(rst)

# 匹配中文(表示范围[u4e00-u9fa5])
title = '世界 你好, hello world'
p2 = re.compile('[\u4e00-\u9fa5]+')
rst1 = p2.findall(title)
print(rst1)

# 贪婪和非贪婪
title1 = '<div>name</div><div>age</div>'
p3 = re.compile('<div>.*</div>')    # 匹配以<div>开头,以</div>结尾,中间可以有的最大内容
p4 = re.compile('<div>.*?</div>')   # 匹配以<div>开头,以</div>结尾,最少内容
m3 = p3.search(title1)
print(m3.group())
m4 = p4.search(title1)
print(m4.group())
