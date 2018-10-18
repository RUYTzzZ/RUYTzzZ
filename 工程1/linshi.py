# -*- coding: utf-8 -*-

import sys
import time
import socket
import requests


import threading

def rw(i):
    for a in range(5):
          print i
          time.sleep(1)

arr=[1,2,3,4,5,6,7]
threads = []  
for i in range(5):


    i = threading.Thread(target=rw,args=(arr[i],))

    threads.append(i)



print threads

for i in threads:

        i.start()
for i in threads:

        i.join()    
