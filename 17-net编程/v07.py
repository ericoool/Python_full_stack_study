#导入相应的包
import smtplib
from email.mime.text import MIMEText
# MIMEText三个主要参数
# 1. 邮件内容
# 2. MIME子类型,在此案例我们用plain表示text类型
# 3. 邮件编码格式

msg = MIMEText("Hello, i am v07", "plain", "utf-8")

# 用来发送email的地址
from_addr = "191169906@qq.com"
# 密码一般需要临时输入,此处是经过申请设置后的授权码
from_pwd = "qoyctsoasxdfbigd"

# 收件人信息
# 此处使用同样的邮箱,给自己发送
to_addr = "191169906@qq.com"

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值
# 采用第三方收发邮件,同样需要在邮件设置中心开启授权选项
# qq邮箱的SMTP地址是 smtp.qq.com
smtp_srv = "smtp.qq.com"

try:
    # 两个参数
    # 1. 服务器地址,但一定要是bytes格式,所以需要编码
    # 2. 服务器的接收访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)  # SMTP协议默认端口25
    # 登陆邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接收地址,必须是list形式
    # 3. 发送内容,以字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    print("邮件发送成功!")
    srv.quit()
except Exception as e:
    print(e)