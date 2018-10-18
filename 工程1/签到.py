# -*- coding: utf-8 -*-

import sys
import time
import socket
from datetime import datetime, timedelta
from time import sleep


def doFirst():        #定时模块
    curTime = datetime.now()
    print curTime
    desTime = curTime.replace(hour=6, minute=31, second=0, microsecond=0)
    print desTime
    delta = desTime-curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" %     sleeptime
    sleep(sleeptime)



def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")

def hqpz():     

    message ='GET /huanghuai/libraryAppointmentOrder_getAppoint?cardnum=YKT'+str(xh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
    
    
    
    try:                
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
            s.close()
            printcn("socket  正在重建")
           
    
    
    
     
    try:               
        host = 'mob.huanghuai.edu.cn'

        remote_ip= socket.gethostbyname( host )
        socket.gethostbyname( host )               
    except:
        s.close()  
    ip=remote_ip  
    try:       
        
        s.connect((ip,80))
    except:
        s.close()
          
    try :
           
          s.sendall(message) 
    except:
         
          s.close()
    reply = s.recv(1024)
    s.close()
    if '"status":"false"' in reply:
       
        printcn ('获取凭证失败\r\n')
       
 
    if '"status":"true"' in reply:
        printcn ('获取凭证')  
        pz1=reply[369:384]
        pz=filter(str.isdigit, pz1)
        printcn(pz)
        printcn(reply[422:434])
        return pz
  
def qiandao(pz):      #签到模块

    message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_sign?appointId='+str(pz)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
    
    
    
    try:                 #创建socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
            s.close()
            printcn("socket  正在重建")
           
    
    
    
     
    try:                  #解析地址端口
        host = 'mob.huanghuai.edu.cn'

        remote_ip= socket.gethostbyname( host )
        socket.gethostbyname( host )
    
                 
    except:
        s.close()
        
    
    ip=remote_ip
    
    try:        # 连接服务器
        
        s.connect((ip,80))
    except:
        s.close()
          
    try :
           #Set the whole string
          s.sendall(message) 
    except:
          #Send failed
          s.close()
    reply = s.recv(1024)
    
    s.close()
   
    if '预约开始后' in reply:
        printcn ('失败 ，签到时间未到\r\n')
     
    if '失败' in reply:
        printcn ('失败 ，检查凭证是否正确  你输入的凭证为'+str(pz)+'\r\n')
        
    if '成功' in reply:
        printcn ('签到成功   '+str(pz)+'\r\n')  

a=0
while a<60:

    xhs=[1534130209,1534130223,1534130121,1534130127,1534130129,1534130131,1534130130,1534130132,1534130208,1534130211,1534130215,1534130216,1534130217,1534130226,1534130227,1534130229]
    #xhs=[1534130121]

    for i in xhs:
       print i
       xh=i
      
       qiandao(hqpz())
    a=a+1
    sleep(300)
