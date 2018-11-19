from email.mime.text import MIMEText
from email.header import Header
import smtplib

msg = MIMEText("Hello, i am v10", "plain", "utf-8")

# 添加邮件头信息
header_from = Header("来自秋日森林的邮件<191169906@qq.com>", "utf-8")
msg['From'] = header_from

header_to = Header("发送给快乐101的邮件", "utf-8")
msg['To'] = header_to

header_sub = Header("这是测试邮件v10", "utf-8")
msg['Subject'] = header_sub

# 以下发送邮件同v07
from_addr = "191169906@qq.com"
from_pwd = "qoyctsoasxdfbigd"
to_addr = "191169906@qq.com"
smtp_srv = "smtp.qq.com"

try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    print("邮件发送成功!")
    srv.quit()
except Exception as e:
    print(e)