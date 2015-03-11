
# -*- coding: utf-8 -*-
import dhtreader
import os
import time

type = 11
pin =26

while True:
  os.system("clear")
  if 0 == dhtreader.init():
    print("init error")

  sensor_val = dhtreader.read(type, pin)
  if sensor_val:
    t,h = sensor_val
    print("{0} {1}".format(t,h))
  else:
    print("error") 

  time.sleep(3)  
  continue