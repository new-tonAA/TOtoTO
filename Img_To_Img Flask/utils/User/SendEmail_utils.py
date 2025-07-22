from email.mime.text import MIMEText
from email.header import Header
import base64
import smtplib
import random

def encode_header(name):
    encoded_name = base64.b64encode(name.encode('utf-8')).decode('utf-8')
    return f'=?utf-8?b?{encoded_name}?='

def SendEmail(email):
    mail_host = "smtp.qq.com"
    mail_user = '1554876672@qq.com'
    mail_pass = ''  # 授权码

    sender = '1554876672@qq.com'  #发件人
    receivers = [email]   #收件人

    from_name = encode_header('Img_To_Img')

    verification = str(random.randint(100,1000))

    message = MIMEText(f"Img_To_Img 登录验证码为{verification}", 'plain', 'utf-8')
    message['From'] = f'{from_name} <{sender}>'  # 发件人
    message['To'] = Header(email)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    subject = '验证码'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 发送邮件
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('邮件发送成功')
        return verification
    except smtplib.SMTPException as e:  # 突发情况
        print(f'邮件发送失败,错误信息:{str(e)}')
        return None