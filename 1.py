#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import socket
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime, timedelta
from time import sleep
import  threading


xh=1534130129
zwh=102110842488
sjr="1570044080@qq.com"




message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_appointSeat?cardnum=YKT'+str(xh)+'&seatId='+str(zwh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'



def doFirst():        #定时模块
    curTime = datetime.now()
    print curTime
    desTime = curTime.replace(hour=21, minute=57, second=21, microsecond=0)
    print desTime
    delta = desTime-curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" %     sleeptime
    sleep(sleeptime)

def mail(my_txt):
   try:
     _user = "hhulibrary@foxmail.com"
     _pwd = "jeevkarioentcije"
     _to =sjr

     msg = MIMEText(my_txt)
     msg["Subject"] ="预约的通知"
     msg["From"] = _user
     msg["To"] = _to

   
     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
     s.login(_user, _pwd)
     s.sendmail(_user, _to, msg.as_string())
     s.quit()
     print "Success!"
   except:
     print "Falied"


def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")


def fabao():
 b=0
 c=0
 i=0
 one=1
 
 while 1:
    
    
    
    
    try:                 #创建socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            i=i+1
            printcn("socket 接口创建" + str( i))
    except:
            s.close()
            printcn("socket  创建失败  " + str( i))
            printcn("socket  正在重建")
            time.sleep(0.1)
            continue
           
    
    
    if one:
     one=0
     try:                  #解析地址端口
        host = 'mob.huanghuai.edu.cn'

        remote_ip= socket.gethostbyname( host )
        socket.gethostbyname( host )
        print remote_ip
        
        printcn("解析服务器地址成功"    )     
        printcn(  str(host) +  "  "  + str(remote_ip))
         
     except:
        s.close()
        printcn("无法解析服务器地址 请检查网络")     
        printcn("即将尝试重启socket")  
        time.sleep(0.1)
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
        time.sleep(0.1)
        continue
    
    a = 0
    while a <10:
	
	
     a=a+1
     try :
           #Set the whole string
          time.sleep(0.05)
          printcn("数据即将发送 "+'学号'+str(xh)+'         ' + str(b+1))
          s.sendall(message) 
          b=b+1
          printcn('数据已经发送  ' +'座位号'+str(zwh)+'    ' + str(b))
     except:
          #Send failed
          c=c+1
          printcn("发送失败" + str(c))
          s.close()
          time.sleep(0.03)
          continue


def jiancha():
  one_1=1

  while 1:
    
    time.sleep(1)


    try:                 #创建socket
            s_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            printcn("socket检测 接口创建" )
    except:
            s_1.close()
            printcn("socket检测  创建失败  " )
            printcn("socket检测  正在重建")
            continue
           
    
    
    if one_1:
     one_1=0
     try:                  #解析地址端口
        host_1 = 'mob.huanghuai.edu.cn'

        remote_ip_1= socket.gethostbyname( host_1 )
        socket.gethostbyname( host_1 )
        print remote_ip_1
        
        printcn("解析服务器地址成功"    )     
        printcn(  str(host_1) +  "  "  + str(remote_ip_1))
         
     except:
        s_1.close()
        printcn("无法解析服务器地址 请检查网络")     
        printcn("即将尝试重启socket")  
        one_1=1   
        continue
     
    
    ip_1=remote_ip_1
    
    try:        # 连接服务器
        
        s_1.connect((ip_1,80))
        printcn("连接至服务器"   + str(remote_ip_1) +"成功"  ) 
    except:
        printcn("服务器无法链接  检查服务器状态")     
        printcn("即将尝试重启socket") 
        s_1.close()
        continue
    

    try :
           #Set the whole string
          s_1.sendall(message) 
    except:
          #Send failed
        
          s_1.close()
          continue

   
   
    reply_1 = s_1.recv(2048)
    s_1.close()
    printcn (reply_1)
    time.sleep(1)
    reply1_1=reply_1[295:]
    printcn (reply1_1) 

    if '冻结' in reply1_1:
           printcn("账户被冻结 需要更换账号")
           my_txt='学号'+str(xh)+'冻结状态  失败 即将退出'
           mail(my_txt)
           break
    if '成功' in reply1_1:
           printcn("预约成功 ")
           my_txt='学号'+str(xh)+'如果你幸运的看到了这封邮件\r\n那么希望已经预约成功了，你可以观察预约一下预约时间是否为你所预期的，在此刻之后 ，系统将会尝试继续锁定十五分钟，十五分钟内你可以尝试通过取消预约来重置预约状态'
           mail(my_txt)
           
           ys=0
           while ys<900:
                ys=ys+1
                ysjs=900-ys
                time.sleep(1)
                printcn('预约成功 *************延时锁定状态 ********* 延时计数'+str(ysjs))
           printcn('延时计数归零  即将退出')
           break

    if '用户已经选择座位' in reply1_1:
           printcn("预约成功")
           my_txt='学号'+str(xh)+'如果你幸运的看到了这封邮件\r\n那么希望已经预约成功了，你可以观察预约一下预约时间是否为你所预期的，在此刻之后 ，系统将会尝试继续锁定十五分钟，十五分钟内你可以通过尝试取消预约来重置预约状态'
           mail(my_txt)
           
           ys=0
           while ys<900:
                ys=ys+1
                ysjs=900-ys
                time.sleep(1)
                printcn('预约成功 *************延时锁定状态 ********* 延时计数'+str(ysjs))
           printcn('延时计数归零  即将退出')
           break

          
    if '座位已经被选择' in reply1_1:
      
           printcn("****************************继续运行中****************************。\r\n\r\n" )





threads = []
t1 = threading.Thread(target=fabao)
threads.append(t1)
t2 = threading.Thread(target=jiancha)
threads.append(t2)



if __name__ == '__main__':
    

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()    
