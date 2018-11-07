import functools
from functools import reduce
# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x-y
# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd, [1,2,3,4,5,6])
print(rst)
print("-"*20)

# 闭包:
def count1():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count1()
print(f1(),f2(),f3())
print("-"*20)

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f4,f5,f6 = count2()
print(f4(),f5(),f6())
print("-"*20)

#装饰器:
import time
# 高阶函数,以函数作为参数
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time: ", time.ctime())
        return f(*args,**kwargs)
    return wrapper
# 上面定义了装饰器,打印当前时间
# 使用的时候需要用到@,此符号是python的语法糖
@printTime
def hello():
    print("Hello World")
hello()
print("-"*20)
def hello2():
    print("手动执行装饰器")
hello2 = printTime(hello2)
hello2()
print("-"*20)
f = printTime(hello2)
f()
print("-"*20)

# 偏函数
print(int("12345"))    # 把字符串转化成十进制数字
print(int("12345",base=8))     # 把八进制的字符串转化成十进制的数字
def int16(x, base=16):  # 新建一个函数,默认输入的16进制字符串,返回十进制数字
    return int(x, base)
print(int16("12345"))
int16_ = functools.partial(int,base=16)
print(int16_("12345"))
print("-"*20)

# enumerate对可迭代对象里的每个元素,配上一个索引,然后索引和内容构成tuple类型
l1 = [11,22,33,44,55]
em1 = enumerate(l1)
l2 = [i for i in em1]
print(l2)

# 可以设置索引的起始
em2 = enumerate(l1, start=1)
l3 = [i for i in em2]
print(l3)
print("-"*20)

# collections模块
## namedtuple包
import collections
Circle = collections.namedtuple("Circle", ['x', 'y', 'r'])  # 定义一个圆,有x,y坐标和r半径
c = Circle(100,150,50)      #实例化
print(c.x)
print(c.y)
print(c.r)
## deque:解决了列表频繁的删除和插入带来的效率问题
from collections import deque
q = deque(['a','b','c'])
q.append('d')   # 在结尾添加
q.appendleft('x')
print(q)
## defaultdict:当直接读取dict不存在的值时,直接返回默认值
from collections import defaultdict
d1 = {'one':1, 'two':2, 'three':3}
func = lambda: "没找到"
d1 = defaultdict(func)
print(d1["four"])
## counter:统计字符串中元素的数量
from collections import Counter
c = Counter("azxhjhglfvjhvkhgvjh")
print(c)