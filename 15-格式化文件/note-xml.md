# 结构化文件储存
- xml, json
- 为了解决不同设备之间的信息交换
# XML文件
- 参考资料:
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
- XML(eXtensibleMarkupLanguage)可扩展的标记语言
    - 标记语言: 语言中使用尖括号括起来的文本字符串标记
    - 可扩展: 用户可以自己定义需要的标记
    - 例如:
    -       <Teacher>
                自定义标记Teacher
                在两个标记之间任何内容都应该跟Teacher相关
            </Teacher>
    - 是w3c组织制定的一个标准
    - XML描述的是数据本身,即数据的结构和语义
    - HTML侧重于如何显示web页面中的数据
    - CSS负责页面效果的控制
    - JS(JavaScript)具有一定功能
- XML文档的构成:
    - 处理指令(可以认为一个文件内只有一个处理指令)
        - 以xml关键字开头
        - 一般用于声明XML的版本和采用的编码
            - version属性是必须的
            - encoding属性用来指出xml解释器使用的编码
    - 根元素(一个文件内只有一个根元素)
        - 在整个xml文件,可以看作一个树形结构
        - 根元素有且只能有一个
    - 子元素
    - 属性
        - 对标签进行说明,一般写在根标签中
    - 内容
        - 标签所存储的信息
    - 注释
        - 注释不能在标签里
        - 在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释的开头,而不能用在结尾
        
                <!--注释内容-->
- 保留字符的处理
    - 使用实体引用(EntityReference)来表示保留字符
    
            <score> score>80 </score>       # 有错误,大于符号>产生冲突
            <score> score&gt;80 </score>    # 使用实体引用
    - 把含有保留字符的部分放在CDATA块内部:
    
            <![CDATA[
                select name,age
                from Student
                where score>80
                ]]>
    - 常用的需要转义的保留字和对应的实体引用
    
            - &: &amp;
            - <: &lt;
            - >: &gt;
            - ': &apos;
            - ": &quot;
            - 一共五个,每个实体引用都以&开头,并且以分号;结尾
- XML标签的命名规则
    - Pascal命名法
    - 单词第一个字母大写
    - 大小写区分
    - 配对标签严格一致
- 命名空间
    - 为了防止命名冲突
    
            <Student>
                <Name>Eric</Name>
                <Age>24</Age>
            </Student>
            <Room>
                <Name>1024</Name>
                <Location>10-2-4</Location>
            </Room>
    - 如果归并上述两个内容,Name标签会产生冲突,需要给可能的冲突元素添加命名空间
    - xmlns: xml name space的缩写
    
            <School xmlns:student="http://my_student" xmlns:room="http://my_room">
                <student:Name>Eric</student:Name>
                <Age>24</Age>
       
                <room:Name>1024</room:Name>
                <Location>10-2-4</Location>
            </School>
# XML访问
## 读取
- XML读取分两个主要技术:
    - SAX(Simple API for XML)
        - 基于事件驱动的API
        - 利用SAX解析文档涉及到解析器和事件处理两部分
        - 特点:
            - 快
            - 流式读取
- DOM
    - 是W3C规定的XML编程接口
    - 一个XML文件再缓存中以树形结构保存,读取
    - 用途:
        - 定位浏览XML任何一个节点信息
        - 添加删除相应内容
    - minidom
        - minidom.oarse(filename): 加载读取的xml文件,filename也可以是xml代码
        - doc.documentElement: 获取xml文档对象,一个xml文件只有一个对应的文档对象
        - node.getAttribute(attr_name): 获取xml节点的属性值
        - node.getElementByTagName(tage_name): 得到一个节点对象集合
        - node.childNodes: 得到所有子节点
        - node.childNodes[index].nodeValue: 获取单个节点值
        - node.firstNode: 得到第一个节点,等价于node.childNodes[0]
        - node.attributes[tage_name]
        
    - etree
        - 以树形结构来表示xml
        - root.getiterator: 得到相应的可迭代的node集合
        - root.iter
        - find(node_name): 查找指定node_name的节点,返回一个node
        - root.findall(node_name): 返回所有node_name的节点
        - node.tag: node对应的tagename
        - node.text: node的文本值
        - node.attrib: 是node的属性的字典类型的内容
        - >案例v02
        
                import xml.etree.ElementTree

                root = xml.etree.ElementTree.parse("school.xml")
                print("利用getiterator访问: ")
                nodes = root.getiterator()
                for node in nodes:
                    print("{0}---{1}".format(node.tag, node.text))
                
                print("利用find和findall方法: ")
                ele_teacher = root.find("Teacher")
                print(type(ele_teacher))
                print("{0}---{1}".format(ele_teacher.tag, ele_teacher.text))
                
                ele_stus = root.findall("Student")
                print(type(ele_stus))
                for ele in ele_stus:
                    print("{0}---{1}".format(ele_stus.tag, ele_stus.text))
                    for sub in ele.getiterator():
                        if sub.tag == "Name":
                            if "Other" in sub.attrib.keys():
                                print(sub.attrib['Other'])
    - xml文件写入
        - 更改
            - ele.set: 修改属性
            - ele.append: 添加子元素
            - ele.remove: 删除元素
        - 生成创建
            - SubElement
            - minidom写入
            - etree写入

