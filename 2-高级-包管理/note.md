# 1. 模块
- 一个模块就是一个包含python代码的文件,后缀名是.py就可以
- 为什么我们用模块
    - 程序太大,编写维护非常不方便,需要拆分
    - 模块可以增加代码复用
    - 当作命名空间使用,避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件,所以任何代码可以直接书写
    - 不过根据模块的规范,最好在模块中编写以下内容:
        - 函数(单一功能)
        - 类(相似功能的组合,或者类似业务模块)
        - 测试代码
- 如何使用模块
    - 模块直接导入
        - 假如模块名称以数字开头,需要借助importlib帮助
    - 语法
    
            import module_name
            module_name.function_name
            module_name.class_name
            案例p01,p02
    - import 模块 as 别名
    - form 模块 import 方法名\类名
- `if __name__ == "__main__":`的使用
    - 可以有效避免模块被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口
    
# 2. 模块的搜索路径和储存
- 什么时模块的搜索路径
    - 加载模块的时候,系统会在那些地方寻找此模块
- 系统默认的模块搜索路径

        import sys
        sys.path 属性可以获取路径列表
- 添加搜索路径

        sys.path.append(dir)
- 模块的加载顺序
    1. 搜索内存中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path列表顺序

# 3. 包
- 包是一种组织管理代码的方式,包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

        |---包
        |---|---__init__.py 包的标志文件
        |---|---模块1
        |---|---模块2
        |---|---子包(子文件夹)
        |---|---|---__init__.py 包的标志文件
        |---|---|---子包模块1
        |---|---|---子包模块2
- 包的导入操作
    - import package_name
        - 直接导入一个包,可以使用__init__.py中的内容
        - 使用方式是:
        
                package_name.func_name
                package_name.class_name.func_name()
        - 注意此种方式是默认对__init__.py内容的导入
    - import package_name as p
        - 别名方式导入
        - 用法和作用方式同上
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.func()
                package.module.class.var
        
# 4. 异常处理
- 广义上的错误分为错误和异常
- 错误指的是可以人为避免
- 异常是指在语法逻辑正确的前提下,出现的问题
- 在python里,异常是一个类,可以处理和使用
- 流程:
    1. 执行try线面的语句
    2. 如果出现异常,则在except语句里查找对应异常并进行处理
    3. 如果没有出现异常,则执行else语句内容
    4. 最后,不管是否出现异常,都要执行finally语句
- 除except(最少一个)以外,else和finally可选

        # 简单异常案例
        # 给出提示信息
        try:
            num = int(input("input a number:"))
            rst = 100/num
            print("计算结果是:{0}".format(rst))
        # 上面的代码可能会出现输入为0,产生除0计算异常
        # 捕获此异常并实例化e
        except ZeroDivisionError as e:
            print(e)    # 可以直接打印实例化e的信息
            exit()      # 然后退出整个程序
        # 如果有多个异常,越具体的异常放最前面
        except NameError as e:
            print("名字起错了")
            print(e)
        except AttributeError as e:
            print("好像属性有问题")
            print(e)
        # 所有异常都继承自Exception类
        # 如果最后写上Exception,任何异常都会截住:
        except Exception as e:
            print("我也不知道哪里出错了")
            print(e)
- 用户手动引发异常
    - 当某些情况,用户希望自己引发一个异常的时候,可以使用
    - raise关键字来引发异常
    
            try:
                print(3.1415926)
                # 手动引发异常
                raise ValueError
                print("没完了")    #这句不会被执行了
            except NmaeError as e:
                print("不会被执行")
            except ValueError as e:     # 执行手动抛出的指定异常
                print(e)
            except Excepttion as e:
                print("不会被执行")
            finally:
                print("我肯定会被执行")
    - 推荐使用自定义异常,必须是系统异常的子类,但方便扩展内容:
      
            
            class UserValueError(ValueError):
                pass    # 继承自系统异常类,可以扩展额外的语句
            try:
                print(3.1415926)
                # 手动引发自定义异常
                raise UserValueError
            except UserValueError as e:     # 执行手动抛出的指定异常
                print(e)
            finally:
                print("我肯定会被执行")

# 5. 常用模块
- calender
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
## calendar
- 跟日历相关的模块
- 有三个参数```cal = calendar.calendar(w, l, c)```
- w = 每个日期之间的间隔字符串
- l = 每周所占用的行数
- c = 每月之间的间隔字符数
- 函数:
    - ``isleap(year)``: 判断某一年是否是闰年
    - ``leapdays(year1,year2)``: 获取指定年份之间的闰年的数量
    - ``month(year,month)``: 获取某个月的日历字符串
    - ``monthrange(year, month)``: 获取一个月的周几开始和天数
    - ``monthcalendar(year, month)``: 返回一个月每天的矩阵列表
    - ``prcal(year)``: print calendar 直接打印一年的日历
    - ``weekday(year, month, day)``: 获取周几
## time
- 时间戳
    - 一个时间表示,根据不同语言,可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
- 时间元组
    - 一个包含时间内容的普通元组
- 函数:
    - ``timezone()``: 当前时区和UTC时间相差的秒数,东八区是-28800固定数值
    - ``localtime()``: 得到当前的时间结构
    - ``asctime()``: 返回元组的正常字符串化后的时间结构
    - ``ctime()``: 获取字符串化的当前时间
    - ``mktime()``: 使用时间元组获取对应的时间戳
    - ``sleep()``: 使程序休眠n秒
    - ``strftime()``: 将时间元组转化为自定义的字符串格式
## os
- 跟操作系统相关,主要使文件操作
- 主要包含在三个模块里
    - os: 操作系统目录相关
    - os.path: 系统路径相关操作
    - shutil: 高级文件存在,目录树的操作,文件赋值,删除,移动
- 路径:
    - 绝对路径: 总是从根目录开始
    - 相对路径: 以当前环境为开始的一个相对的路径
- 函数:
    - ``getcwd()``: 获取当前工作目录
    - ``chdir()``: 改变当前工作目录
    - ``listdir()``: 获取一个目录中所有子目录和文件的名称列表
    - ``makedirs()``: 创建文件夹
    - ``exit()``: 退出当前程序
## shutil
- 函数:
    - ``copy()``: 复制文件,在拷贝的同时,可以给文件重命名
    - ``copyfile()``: 将一个文件中的内容复制到另一个文件当中
    - ``move()``: 移动文件/文件夹
## 归档和压缩
- 归档: 把多个文件或者文件夹合并到一个文件当中
- 压缩: 用算法把多个文件或者文件夹有损或无损的合并到一个文件当中
- 函数:
    - ``make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')``: 归档操作.
    - ``unpack_archive('归档文件地址','解包之后的地址')``: 解包操作.
## random
- 随机数
- 所有的随机模块都是伪随机
- 函数:
    - ``random.random()``: 获取0-1之间的随机小数
    - ``random.choice(序列)``: 随机返回序列中的某个值
    - ``random.shuffle(列表)``: 随机打乱列表
    - ``random.randint(a,b)``: 返回一个a到b之间的随机整数,包含a和b