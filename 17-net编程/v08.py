from email.mime.text import MIMEText

mail_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>这是一封HTML格式邮件v08</h1>
    </body>
    </html>
    """

msg = MIMEText(mail_content, "html", "utf-8")

# 构建发送者地址和登陆信息
from_addr = "191169906@qq.com"
from_pwd = "qoyctsoasxdfbigd"
to_addr = "191169906@qq.com"
smtp_srv = "smtp.qq.com"

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    print("邮件发送成功!")
    srv.quit()
except Exception as e:
    print(e)