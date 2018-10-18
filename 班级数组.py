#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import re
f = open('/Users/OoO/Desktop/banji.txt')
s=f.read()
s1 = re.split(r" +", s) #利用正则函数进行分割
for i in s1:
      s2=i[0:6]
      print s2
      while a<999:
          a=a+1
          xh=s2+9

