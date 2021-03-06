'''
1. 需求:
现在有以下几个日志记录的需求:
    1) 要求将所有级别的日志都写入磁盘文件中
    2) all.log文件中记录所有的日志信息,日志格式为: 日期和时间 - 日志级别 - 日志信息
    3) error.log文件中单独记录error及以上级别的日志信息,日志格式为: 日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
    4) 要求all.log在每天凌晨进行日志切割

2. 分析:
    1) 要记录所有级别的日志,因此日志器的有效level需要设置为最低级别--DEBUG
    2) 日志要求被发送到两个不同的目的地,因此需要为日志设置两个handler; 另外,两个目的地都是磁盘文件,因此这两个handler都是与Filehandler
    3) all.log要求按照时间进行切割,因此需要用logging.hanglers.TimeRotatingFileHandler;而error.log没有要求
    4) 两个日志文件的格式不同,因此需要对这两个Handler分别设置格式器
'''

import logging
import logging.handlers
import datetime

# 定义一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 为两个不同的文件设置不同的handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=None)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 把相应的处理器组装到logger上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug("This is a debug log.")
logger.info("This is a info log.")
logger.warning("This is a warning log.")
logger.error("This is a error log.")
logger.critical("This is a critical log.")
