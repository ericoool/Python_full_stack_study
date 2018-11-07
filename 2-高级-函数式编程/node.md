## log模块资料
- https://www.cnblogs.com/yyds/p/6901864.html
# 函数式编程(Functional Programming)
- 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数,同样可以作为返回值
    - 纯函数式编程语言: LISP, Haskell
- Python函数式编程只是借鉴函数式编程的一些特点,可以理解为一半函数式一般Python
- 需要讲述:
    - 高阶函数
    - 返回函数
    - 匿名函数
    - 装饰符
    - 偏函数
## lambda表达式
- 函数: 最大程度复用代码
    - 存在问题: 如果函数很小,很短,则会造成啰嗦
    - 如果函数被调用次数少,则会造成浪费
- lambda表达式(匿名函数):
    - 一个表达式,函数体相对简单
    - 不是一个代码块,仅仅使一个表达式
    - 可以有参数,有多个参数也可以,用逗号隔开
    - 用法:
        - 以lambda开头
        - 紧跟参数(可以没有)
        - 参数后用冒号与表达式主体隔开
        - 只是一个表达式,所以没有return
        -       stm = lambda x: 100 * x
                stm(36)
                >>>3600     #使用上和函数的调用一样
                stm2 = lambda x,y,z: x+y*10+z*100
                stm2(2,4,6)
                >>>642
## 高阶函数
- 把函数作为参数使用的函数,叫高阶函数
### 系统高阶函数-map
- 原意就是映射,即把集合或则列表的元素,每个元素都按照一定规则进行操作,生成一个新集合或者列表
- map函数使系统提供的具有映射功能的函数,返回值是一个迭代对象
- map是一个可迭代的类型
- map(func, *iterables可迭代参数) --> map object
- 可以用for循环遍历
-       def mulTen(n):
            return n*10
        l1 = [ i for i in range(10)]
        l3 = map(mulTen, l1)    #把l1列表里的每个元素乘以10
        for i in l3:
            print(i)
        #以下打印结果为空列表,why?
        l4 = [i for i in l3]
        print(l4)
### reduce
- 原意是归并,缩减
- 把一个可迭代对象最后归并成为一个结果
- 对于作为参数的函数要求: 必须由两个参数,必须返回结果
- reduce需要导入functools包
-       form functools import reduce
        # 定义一个操作函数
        # 加入操作函数只是相加
        def myAdd(x,y):
            return x+y
        # 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
        rst = reduce(myAdd, [1,2,3,4,5,6])
        print(rst)
        -->21
### filter函数
- 过滤函数:对一组数据进行过滤,符合条件的数据会生成一个新的列表并返回
- 跟map相比较:
    - 相同:都对列表的每一个元素逐一进行操作
    - 不同:
        - map会生成一个跟原来数据相对应的新列表
        - filter不一定,只要符合条件的才会进入新的数据集合
    - filter函数怎么写:
        - 利用给定函数进行判断
        - 返回值一定是布尔值
        - 调用格式:filter(f,data),f是过滤函数,data是数据
        
### 排序
- 把序列按照给定算法进行排序
- key:在排序前对每个元素进行kay函数运算,可以理解成按照kay函数定义的逻辑进行排序
- python2和python3相差巨大
-       a = [234,-353,22,13,456,2,-6,8,3424]
        al1 = sorted(a)     # 正序
        al2 = sorted(a,reverse=True)    #倒序
        al3 = sorted(a,key=abs)         #按绝对值的大小正序
## 返回函数
- 函数可以返回具体的值
- 也可以返回一个函数作为结果
-       def func1():
            def func2():
                print("i am func2")
                return 2
            return func2
        f3 = func1()    # 将func1()函数的返回值赋值给f3
        f3()            # 由于返回值是函数func2(),赋值给f3后,f3()就可以直接调用
        -->i am func2
## 闭包(closure)
- 当一个函数在内部定义函数,并且内部的函数应用外部函数的参数或者局部变量,当内部函数被当作返回值的时候,相关参数和变量保存在返回函数中,这种结果,叫作"闭包"
- 返回闭包的时候,返回函数里面不能引用任何的循环变量
- 案例见01.py
### 装饰器(Decrator)
- 在不改动函数代码的基础上,无限制扩展函数功能的一种机制,本质上,装饰器是一个返回函数的高阶函数
- 装饰器的使用: 
    - 使用@语法,即在每次要扩展到函数定义前使用@+函数名:```@装饰器\n 定义函数func```
    - 手动执行:定义好函数func后,```func = 装饰器(func)```,然后再调用func就能附加上装饰器功能
- 一旦函数被装饰,则把装饰器的功能直接添加到定义函数的功能上
### 偏函数
- 参数固定的函数,相当于一个有固定参数的函数体:``int("n",base=10)``(将一个10进制的字符串转为整数,base是固定参数)
- functools.partial的作用是把一个函数某些参数固定,返回一个新函数
    - 用法:``int16 = functools.partial(int,base=16)``(把int函数的base参数固定,返回一个新函数,赋值给int16)
    - 案例见01.py
### zip
- 把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容
- 建立一一对应的元组
-       l1 = [1,2,3,4,5]
        l2 = [11,22,33,44,55]
        z = zip(l1, l2)
        for i in z:
            print(i)
        -->(1,11)(2,22)(3,33)(4,44)(5,55)
### enumerate
- 跟zip功能比较像
- 对可迭代对象里的每个元素,配上一个索引,然后索引和内容构成tuple类型
-       l1 = [11,22,33,44,55]
        em1 = enumerate(l1)
        l2 = [i for i in em1]
        print(l2)
        -->[(0,11),(1,22),(2,33),(3,44),(4,55)]
        # 可以设置索引的起始
        em2 = enumerate(l1, start=1)
        l3 = [i for i in em2]
        print(l3)
        -->[(1,11),(2,22),(3,33),(4,44),(5,55)]
### collections模块
- namedtuple
- deque
#### namedtuple
- tuple类型
- 是一个可命名的tuple
-       Circle = collections.namedtuple("Circle", ['x', 'y', 'r'])   # 定义一个圆,有x,y坐标和r半径
        c = Circle(100,150,50)      #实例化
        c.x
        c.y
        c.r
#### deque
- 比较方便的解决了列表频繁的删除和插入带来的效率问题
-       q = deque(['a','b','c'])
        q.append('d')   # 在结尾添加
        q.appendleft('x')
#### defaultdict
- 当直接读取dict不存在的值时,直接返回默认值
-       from collections import defaultdict
        d1 = {'one':1, 'two':2, 'three':3}
        func = lambda: "没找到"
        d1 = defaultdict(func)
#### Counter
- 统计字符串中元素的数量
-       from collections import Counter
        c = Counter("azxhjhglfvjhvkhgvjh")
        print(c)
        -->Counter({'h': 5, 'j': 3, 'v': 3, 'g': 2, 'a': 1, 'z': 1, 'x': 1, 'l': 1, 'f': 1, 'k': 1})