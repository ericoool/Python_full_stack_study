# 创建一个类
# 创建一个方法
# 一个打印语句

class Student():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("HI, 欢迎来到图灵学院!")

# 当这个模块被单独执行的时候,才调用.作为模块被import时,不执行下面语句:
# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print("我是模块p01")

