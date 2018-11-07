# 在函数odd中,yield负责返回
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3
g = odd()   # 实例化一个生成器.odd是一个object类
one = next(g)   # 用next调用yield返回的第一个结果
print(one)      # -->Step 1 -->1
two = next(g)   # 用next调用yield返回的第二个结果
print(two)      # -->Step 2 -->2
three = next(g)   # 用next调用yield返回的第三个结果
print(three)      # -->Step 3 -->3

def fib(max):           # 斐波那契数列
    n, a, b = 0, 0, 1
    while n < max:
        yield b         # 用yield每次返回b值
        a, b = b, a+b
        n += 1
    return 'Done'
num = 5
g_fib = fib(num)
ge_fib = fib(num)
for i in range(num):    # 如果循环次数是num+1.则报出异常,返回值是return的Done
    rst = next(g_fib)
    print(rst)
for i in ge_fib:        # 在for循环里直接使用生成器,典型应用
    print(i)