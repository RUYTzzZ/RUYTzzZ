# -*- coding: utf-8 -*-

import sys
import socket
from time import sleep
import time
from datetime import datetime, timedelta


a=1

i=1


def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")

def cxpz(xh):
   message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_getAppoint?cardnum=YKT'+str(xh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   s.connect((socket.gethostbyname('mob.huanghuai.edu.cn' ),80))
   s.sendall(message)
   reply=s.recv(1024)
   s.close()
   if 'buildingName' in reply:
       pz=filter(str.isdigit, reply[365:385])
       print("ok")
       return pz   

def ql(pz):
   message ='GET /huanghuai/libraryAppointmentOrder_close?appointId='+str(pz)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((socket.gethostbyname('mob.huanghuai.edu.cn' ),80))

   s.sendall(message)


   s.close()


def zw(xh):
     message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_appointSeat?cardnum=YKT'+str(xh)+'&seatId='+str(zwh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect((socket.gethostbyname('mob.huanghuai.edu.cn' ),80))

     s.sendall(message)
     reply=s.recv(1024)


  
     s.close()

     if '用户已经' in reply:
         global a
         printcn('结果确认计数   '+str(a)+'   \n\n')
         
         
 

         a=a+1
     else:
         printcn('wrong    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n')
def zw1(xh):
     message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_appointSeat?cardnum=YKT'+str(xh)+'&seatId='+str(zwh)+' HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.connect((socket.gethostbyname('mob.huanghuai.edu.cn' ),80))

     s.sendall(message)
     sleep(0.01)
     s.sendall(message)
     sleep(0.01)
     s.sendall(message)
     sleep(0.01)
     s.sendall(message)

     s.close()

def doFirst():        #定时模块
    curTime = datetime.now()
    print curTime
    desTime = curTime.replace(hour=6, minute=31, second=0, microsecond=0)
    print desTime
    delta = desTime-curTime
    sleeptime = delta.total_seconds()
    print "Now day must sleep %d seconds" %     sleeptime
    sleep(sleeptime)





doFirst()
while i<300:
    xh=1534130226
    zwh=10211084832


    printcn('执行计数       '+str(i)+'')

    ql(cxpz(xh))
    zw1(xh)
    zw1(xh)
    zw1(xh)
    zw(xh)
    i=i+1
    sleep(180)


raw_input("Press <enter>")
