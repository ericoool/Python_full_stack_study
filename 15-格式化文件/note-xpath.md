# XPath
- 在xml文件中查找信息的一套规则/语言,根据xml的元素或者属性进行遍历
- 参考: http://www.w3school.com.cn/xpath/index.asp

# XPath开发工具
- 开源的XPath表达式编辑工具: XMLQuire
- Chrome插件: XPath Helper
- FireFox插件: XPath Checker

# 选取节点
- nodename: 选取次节点的所有子节点
- /: 从根节点开始选取
- //: 选取节点,不考虑位置
- .: 选取当前的节点
- ..: 选取当前节点的父节点
- @: 选取属性

# 谓语-Predicates
- /School/Student[1]: 选取School下面第一个Student节点
- //Student[@score]: 选取带有属性score的Student节点
- //Student[@score="99"]/age: 选取带有属性score=99的Student节点的子节点age

# XPath的一些操作
- |: 或者
    - //Student[@score] | //Teacher: 选取带有属性score的Student节点和Teacher节点
- 其余不常见XPath运算符号包括+,-,*,/    