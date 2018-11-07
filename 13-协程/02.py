# 协程代码案例
def simple_coroutine():
    print('-> start')
    x = yield               # 第一次调用yield返回空
    print('->recived', x)   # 第二次调用,x=yield返回send的参数

# 主线程
sc = simple_coroutine()
print(1111)
next(sc)    # 预激: 可以使用sc.send(None),效果一样
print(2222)
sc.send('recall')