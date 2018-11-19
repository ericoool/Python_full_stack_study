from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase, MIMEMultipart

mail_mul = MIMEMultipart()
# 构建邮件正文
mail_text = MIMEText("Hello, i am v09", "plain", "utf-8")
# 把构建好的邮件正文附加入邮件
mail_mul.attach(mail_text)

# 构建附件
# 需要从本地读入附件
# 打开一个本地文件
# 以rb格式打开
with open("02.html", "rb") as f:
    s = f.read()
    # 设置附件的MIME和文件名
    m = MIMEText(s, 'base64', 'utf-8')
    m["Content-type"] = "application/octet-stream"
    # 需要注意
    # 1. attachment后分号为英文状态
    # 2. filename后面需要用引号包裹,注意与外面的引号错开
    m["Content-Disposition"] = "attachment; filename='02.html'"
    # 添加到MIMEMultipart
    mail_mul.attach(m)

# 上面邮件内容构造完毕,发送邮件同v07
from_addr = "191169906@qq.com"
from_pwd = "qoyctsoasxdfbigd"
to_addr = "191169906@qq.com"
smtp_srv = "smtp.qq.com"

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], mail_mul.as_string())
    print("邮件发送成功!")
    srv.quit()
except Exception as e:
    print(e)