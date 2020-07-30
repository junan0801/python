import smtplib
from email.mime.text import MIMEText
from email.header import decode_header
mail_host = 'smtp.qq.com'
mail_user = '12109052759@qq.com'
mail_pass = 'symvytijjqnxhfaj'
sender = '1219052759@qq.com'
receivers = ['656540580@qq.com']
massage = MIMEText('测试邮件', 'plain', 'utf8')
message['rom'] = decode_header('菜鸟教程')
#message['to'] = decode_header('测试')
subject = 'python SMTP 测试'
#message['subject'] = decode_header(subject)

