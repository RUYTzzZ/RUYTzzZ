
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import socket
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime, timedelta
from time import sleep



my_user='1570044080@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
my_sender='15649566613@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量

my_txt='           dsfdfs'
def mail():
    ret=True
    try:
        msg=MIMEText(str(my_txt) ,'plain','utf-8')
        msg['From']=formataddr(["",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="预约通知" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"ws970320")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret
ret=mail()
if ret:
    print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
else:
    print("filed")  #如果发送失败则会返回filed