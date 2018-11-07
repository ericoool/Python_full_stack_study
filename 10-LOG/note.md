# LOG
- http://www.cnblogs.com/yyds/p/6901864.html
- loogging模块: 提供模块级别的函数记录日志
- 包括四大组件

## 1. 日志相关概念
- 日志
- 日志的级别
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作-->不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# 2. logging模块
- 日志级别
    - 级别可以自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别, 只有当级别等于或者高于指定的级别才被记录
- 使用方式
    - 直接使用logging(封装了其他组件)
## 2.1 logging模块级别的日志
- 使用以下几个函数:
    - logging.debug(msg, *args, **kwargs) 创建一条级别为DEBUG的日志记录
    - logging.info(msg, *args, **kwargs) 创建一条级别为INFO的日志记录
    - logging.warning(msg, *args, **kwargs) 创建一条级别为WARNING的日志记录
    - logging.error(msg, *args, **kwargs) 创建一条级别为ERROR的日志记录
    - logging.critical(msg, *args, **kwargs) 创建一条级别为CRITICAL的日志记录
    - logging.log(level, *args, **kwargs) 自定义创建一条level级别的日志记录
    - logging.basicConfig(**kwargs) 对root logger进行一次性配置
    
- logging.basicConfig(**kwargs) 对root logger进行一次性配置
    - 只在第一次调用时起作用
    - 不配置logger则使用默认值
        - 输出: sys.stderr
        - 级别: WARNING
        - 格式: level:log_name:content
- 案例01,,format的参数自行查询
## 2.2 logging模块的处理流程
- 四大组件
    - 日志器(logger): 产生日志的一个接口
    - 处理器(Handler): 把产生的日志发送到相应的目的地
    - 过滤器(Filter): 更精细的控制那些日志输出
    - 格式器(Formatter): 对输出信息进行格式化
- logger
    - 产生一个日志
    - 操作
    -       Logger.setLevel()   # 设置日志器将会处理的日志消息的最低级别
            Logger.addHandel() 和 Logger.removeHandler()     # 为该logger对象添加和移除一个Handler对象
            Logger.addFilter() 和 logger.removeFilter()      # 为该logger对象添加和移除一个Filter对象
            Logger.debug:   #产生一条debug级别的日志,同理info,error等
            logger.exception():     # 创建蕾仕于Logger.error的日志消息
            Logger.log():   # 或取一个明确的日志level参数类创建一个日志记录
    - 如何得到一个logger对象
        - 实例化
        - logger.getLogger()
- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter, removeFilter
    - 不需要直接使用,Handler是基类
    -       logging.StreamHandler   # 将日志消息发送输出到Stream,如std.out,std.err或任何file-like对象
            logging.FileHandler     # 将日志消息发送到磁盘文件,默认情况下文件大小会无限增长
            logging.handlers.RotatingFileHandler    # 将日志消息发送到磁盘文件,并支持按文件大小切割
            logging.handlers.TimedRotatingFileHandler   # 按文件时间切割
            logging.handlers.HTTPHandler    # 将日志消息以GET或POST的方式发送给一个HTTP服务器
            logging.handlers.SMTPHandler    # 将日志消息发送给一个指定的email地址
            logging.NullHandler     #该Handler实例会忽略error messages,通常被想使用logging的library
- Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数
        - fmt: 
        - datefmt:
        - style:
- Filter类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息的具体内容
    - 案例02