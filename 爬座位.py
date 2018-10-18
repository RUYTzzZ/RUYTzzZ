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

def doFirst():
    curTime = datetime.now()
    print curTime
    desTime = curTime.replace(hour=21, minute=58, second=10, microsecond=0)
    print desTime
    delta = desTime-curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" %     sleeptime
    sleep(sleeptime)

 
 

f=1000
xh=1734130111

sjr='1570044080@qq.com'


one=1
i=0
flag=0
b=0
c=0
timesmg=0







def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")









#doFirst()  #定时模块


#printcn("即将发送启动信息") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
#mail()
  
while f<3000:
    time.sleep(0.1)
    f=f+1
    zwh='10211084'+str(f)
    message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_appointSeat?cardnum=YKT'+str(xh)+'&seatId='+str(zwh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
    try:                 #创建socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            i=i+1
            printcn("socket 接口创建" + str( i))
    except:
            s.close()
            printcn("socket  创建失败  " + str( i))
            printcn("socket  正在重建")
            continue
           
    
    
    if one:
     one=0
     try:                  #解析地址端口
        host = 'mob.huanghuai.edu.cn'

        remote_ip= socket.gethostbyname( host )
        port = 80
        socket.gethostbyname( host )
        print remote_ip
        
        printcn("解析服务器地址成功"    )     
        printcn(  str(host) +  "  "  + str(remote_ip))
         
     except:
        s.close()
        printcn("无法解析服务器地址 请检查网络")     
        printcn("即将尝试重启socket")  
        one=1   
        continue
     
    
    ip=remote_ip
    
    try:        # 连接服务器
        
        s.connect((ip,80))
        printcn("连接至服务器"   + str(remote_ip) +"成功"  ) 
    except:
        printcn("服务器无法链接  检查服务器状态")     
        printcn("即将尝试重启socket") 
        s.close()
        continue
    
    
	
	
     
    try :
           #Set the whole string
          printcn("数据即将发送 "+'学号'+str(xh)+'         ' + str(b+1))
          s.sendall(message) 
          b=b+1
          printcn('数据已经发送  ' +'座位号'+str(zwh)+'     ' + str(b))
    except:
          #Send failed
          c=c+1
          printcn("发送失败" + str(c))
          s.close()
          continue
    reply = s.recv(1024)
    printcn (reply)
    s.close()
    if '操作失败' in reply:
        print 'nonono'
    else:
        print  'yes'   
        
        file = open('/Users/OoO/Desktop/shujuda.txt'.decode('utf-8'),'a')
        file.write('   '+zwh+'   ')
        file.close()

     
    
       
      

