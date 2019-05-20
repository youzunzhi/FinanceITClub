import smtplib
from email.mime.text import MIMEText
from email.header import Header

import time

def SendMail(username, password, to_list, content, subject):
    mail_host = "smtp.163.com"
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = username
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtp_obj = smtplib.SMTP()
        # smtp_obj.set_debuglevel(1)
        smtp_obj.connect(mail_host, 25)
        smtp_obj.login(username, password)
        print('Login Success!')
        for to_addr in to_list:
            message['To'] = to_addr
            smtp_obj.sendmail(username, to_addr, message.as_string())
        print('Send Email Success!')
        smtp_obj.quit()
        print('Done.')
    except smtplib.SMTPException:
        print('SMTPException')

def SendTimingMail(send_hour, send_minute, username, password, to_list, content, subject):
    while True:
        cur_time = time.localtime()
        if (cur_time.tm_hour == send_hour and cur_time.tm_min == send_minute):
            print("Time to send mail.")
            SendMail(username, password, to_list, content, subject)
            break


if __name__ == '__main__':
    username = "youzunzhi@163.com"
    password = input("Input Password: ")
    to_list = ["youzzh@mail2.sysu.edu.cn", "454367695@qq.com"]
    content = "Hi there."
    subject = 'Python Mail Test'

    send_hour = 0
    send_minute = 14

    # SendMail(username, password, to_list, content, subject)
    SendTimingMail(send_hour, send_minute, username, password, to_list, content, subject)

