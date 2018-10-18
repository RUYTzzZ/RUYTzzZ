#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import socket
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime, timedelta
from time import sleep
import  threading

xh=1534130121
zwh=102110842488


while 1:
     try:                 #创建socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

     except:
            s.close()
  
            continue
           
    
    

 
     try:                  #解析地址端口
        host = 'mob.huanghuai.edu.cn'

        remote_ip= socket.gethostbyname( host )
        socket.gethostbyname( host )
        print remote_ip
        

         
     except:
        s.close()

        time.sleep(0.1)
        one=1   
        continue
     
    
    
     try:        # 连接服务器
        
        s.connect((remote_ip,80))
 
     except:

        s.close()
        continue


     message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_appointSeat?cardnum=YKT'+str(xh)+'&seatId='+str(zwh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
     s.sendall(message)
     reply= s.recv(2048)
     print reply
     
     s.sendall(message)
     print reply
     break