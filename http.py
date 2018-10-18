#coding=utf-8
'''
Created on 2015-7-20
@author: xhw
@explain: 实现GET方法和POST方法请求
'''

import sys
import time
import socket
from  BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import urllib
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
        if '失败' in reply:
            printcn ('失败 ，检查凭证是否正确  你输入的凭证为'+str(pz))
            return 0
        if '成功' in reply:
            printcn ('签到成功   '+str(pz))  
            return 1
def printcn(b):         #配置中文输出函数
        sys_encoding = sys.getfilesystemencoding()
        print(b.decode('utf-8').encode(sys_encoding))

   
        reload(sys)
        sys.setdefaultencoding("utf-8")
    
class ServerHTTP(BaseHTTPRequestHandler):
    
    
    
    
    
    
    
    
    
    def do_GET(self):
        path = self.path
        print path
        #拆分url(也可根据拆分的url获取Get提交才数据),可以将不同的path和参数加载不同的html页面，或调用不同的方法返回不同的数据，来实现简单的网站或接口
        query = urllib.splitquery(path)
        print query
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("test","This is test!")
        self.end_headers()
        buf = '''<!DOCTYPE HTML>
                <html>
                <head><title>Get page</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>
                <body>
                
                <form action="post_page" method="post">
                  输入预约凭证: <input type="text" name="id" /><br />
                  <input type="submit" value="POST" />
                </form>
                
                </body>
                </html>'''
        self.wfile.write(buf)
        
    def do_POST(self):
        path = self.path
        print path
        #获取post提交的数据
        datas = self.rfile.read(int(self.headers['content-length']))
        datas = urllib.unquote(datas).decode("utf-8", 'ignore')
        pz=datas[3:]
        print pz
        if qiandao(pz)==1:
              datas2='预约凭证'+str(pz)+'签到成功'
        if qiandao(pz)==0:
              datas2='预约凭证'+str(pz)+'签到失败  ,检查预约状态及凭证准确性' 
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("test","This is test!")
        self.end_headers()
        
              
              
        buf = '''<!DOCTYPE HTML>
        <html>
            <head><title>Post page</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>
            <body>  %s  <br />   %s </body>
        </html>'''%(datas,datas2)
        self.wfile.write(buf)
        
def start_server(port):
    http_server = HTTPServer(('', int(port)), ServerHTTP)
    http_server.serve_forever() 
    
if __name__ == "__main__":
    start_server(8080)
