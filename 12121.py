#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import socket



from datetime import datetime, timedelta
from time import sleep


def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")
a=b=c=i=0
one=1
 
z=26
x=1
c=1
v=1
b=0
n=0


while 1:
    time.sleep(0.01)
    n=n+1
    if n>9:
         b=b+1 
         n=0
         if b>7:
             b=0
             v=v+1
             if v>5:
                 v=1
                 c=c+1
                 if c>7:
                     c=1
                     z=z+1
    
    xh='15'+str(z)+str(x)+str(c)+'0'+str(v)+str(b)+str(n)
    print xh

    message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_historyList?cardnum=YKT'+str(xh)+'&page=1&pageSize=15 HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
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
        
          s.sendall(message) 

          printcn('数据已经发送  ')
    except:
          #Send failed

          printcn("发送失败" + str(c))
          s.close()
          continue
   
   
   
   
    reply = s.recv(2048)
    s.close()
    reply1=reply[295:]
    printcn (reply1)
  
  
    

    if '自习室' in reply:
        print 'need'
        
        file = open('/Users/OoO/Desktop/pz.txt','a')
        
        file.write(xh+reply1)#
        file.close() 
    else:
        print  'not'   
        
   
