#handling errors in python socket programs


flag=1
i=0
import time

while flag:
 
 
 time.sleep( 0.2 )
 import socket   #for sockets
 import sys  #for exit
 
 try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    break   
 
 print 'Socket Created'


 
 
 try:
   host = 'mob.huanghuai.edu.cn'
   port = 80
   remote_ip = socket.gethostbyname( host )
  
 except socket.gaierror:
   
    print 'Hostname could not be resolved. Exiting'
    
     
 print 'Ip address of ' + host + ' is ' + remote_ip
 #Connect to remote server
 s.connect((remote_ip , port))
 
 print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_appointSeat?cardnum=YKT1534130215&seatId=102110841016 HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'
 
 
 a = 0

 while a < 20:
	
	
 
  try :
    #Set the whole string
    s.sendall(message) 
  except socket.error:
    #Send failed
    print 'Send failed'
    flag=0
    flag=1
  print i
  print 'has been sent'
  i += 1
  a += 1
 
  
 
 
 

 s.close()

 print 'The connection has been closed   17'
 
