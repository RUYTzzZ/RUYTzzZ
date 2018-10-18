
import sys
import time
import socket

def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")


def hqpz():     
    message ='GET /huanghuai/libraryAppointmentOrder_getAppoint?cardnum=YKT1534130130 HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
    
    
    
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
    pz=reply[371:382]
    printcn(reply)
    printcn(pz)
    s.close()


hqpz()