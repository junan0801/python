import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 发送邮件服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户名和密码(此密码为在qq邮箱中开启smtp服务后的授权码，不是平时的登录密码)
password = 'symvytijjqnxhfaj'
# 发送邮箱
sender = '1219052759@qq.com'
# 接受邮箱
receiver = '656540580@qq.com'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header('Python 3 smtp', 'utf-8')
message['To'] = Header('测试', 'utf-8')
subject = 'Python SMTP邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是测试Python发送附件功能....', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的test.txt文件
att1 = MIMEText(open('123.txt', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字 邮件中就显示什么名字
att1['Content-Disposition'] = 'attachment;filename="test123.txt"'
message.attach(att1)

smtp = smtplib.SMTP_SSL(smtpserver, 465)
smtp.ehlo()
smtp.login(sender, password)
smtp.sendmail(sender, receiver, message.as_string())
smtp.quit()