from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# 1. 构建一个MIMEMultipart邮件
msg = MIMEMultipart("alternative")

# 1.1 构建一个HTML邮件内容
html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>

    <h1>这是一封HTML格式邮件v11</h1>

    </body>
    </html>
    """
msg_html = MIMEText(html_content, "html", "utf-8")
msg.attach(msg_html)

# 1.2 构建一个text邮件内容
msg_text = MIMEText("这是一封text格式邮件v11", "plain", "utf-8")
msg.attach(msg_text)

# 以上邮件构建完毕,以下发送邮件同v07
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