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

#def doFirst():
    curTime = datetime.now()
    print curTime
    desTime = curTime.replace(hour=21, minute=58, second=10, microsecond=0)
    print desTime
    delta = desTime-curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" %     sleeptime
    sleep(sleeptime)

 
 

sys_encoding = sys.getfilesystemencoding()
xh=1734130708
zwh=10211084145
my_user='1570044080@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
my_sender='15565682763@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量

my_txt='学号'+str(xh)+'座位号'+str(zwh)+'如果你可以足够幸运看到这个邮件，那么说明服务器已经自行启动\r\n 但是在此之前你需要保证的是此学号没有进入预约'
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


def printcn(b):         
   
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")
#中文输入函数
#printcn("中文")




message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_appointSeat?cardnum=YKT'+str(xh)+'&seatId='+str(zwh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
i=0
flag=0
b=0
c=0
timesmg=0

print xh
print zwh
doFirst()  #定时模块


try: 
  mail()
  printcn('已发送通知')
except:
  print'通知失败'
    
while 1:
    time.sleep(0.2)
    
    
    
    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            i=i+1
            printcn("socket 接口创建" + str( i))
    except:
            s.close()
            printcn("socket  失败  " + str( i))
            printcn("socket  正在重建")
            continue
           
    
    
    try:
        host = 'mob.huanghuai.edu.cn'
        host = 'mob.huanghuai.edu.cn'
        
        port = 80
        remote_ip =   socket.gethostbyname( host )
        
        printcn("解析服务器地址成功"    )     
        printcn(  str(host) +  "  "  + str(remote_ip))
    except:
        s.close()
        printcn("无法解析服务器地址 请检查网络")     
        printcn("即将尝试重启socket")     
        continue

    try:
        
        s.connect((remote_ip , port))
        printcn("连接至服务器"   + str(remote_ip) +"成功"  ) 
    except:
        printcn("服务器无法链接  检查服务器状态")     
        printcn("即将尝试重启socket") 
        s.close()
        continue
    
    a = 0
    
    while a <15:
	
	
     a=a+1
     try :
           #Set the whole string
          printcn("数据即将发送  " + str(b+1))
          s.sendall(message) 
          b=b+1
          printcn("数据已经发送  xh=1734130208  zyh=10211084145  " + str(b))
          
         
          

     except:
          #Send failed
          c=c+1
          printcn("发送失败" + str(c))
          s.close()
          continue
    timesmg=timesmg+1   
     
    if timesmg==12 or  timesmg==1:
     try :
       timesmg=2
       reply = s.recv(1024)
       s.close()
       reply1=str(reply)[320:425]
       printcn("********************************************状态展示*********************************************\r\n******************************************* 状态展示*********************************************" )
       printcn(reply1 )
       if '冻结' in reply1:
           printcn("账户被冻结 需要更换账号")
           
           my_txt='账户冻结  无法处理已停止'
           mail()
           flag=1
           break
       if '成功' in reply1:
           printcn("预约成功 ")
           flag=2
           my_txt='预约成功 需要判断自行预约日期'
           mail()
           break

       if '用户已经选择座位' in reply1:
           printcn("预约成功")
           flag=3
           my_txt='你已经选择座位，云端数据发送已停止'
           
           break
          
       if '座位已经被选择' in reply1:
           printcn("     继续运行中。。。。。\r\n\r\n" )
           flag=4
     except:
       timesmg=2
       s.close()
       printcn("状态展示失败")
       continue
      

