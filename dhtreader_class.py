
# -*- coding: utf-8 -*-
import dhtreader
import os
import time

class DhtReader_Class:
  def __init__ (device_type , pin_no):
    self.type  = devise_type
    self.pin   = pin_no

  def init_devise(self):
    os.system("clear")
    return True if 0 == dhtreader.init:
    print("init error")
    return False

  def read_value(self):
    val = None
    for _ in range(10):
      sensor_val = dhtreader.read(type, pin)
      if sensor_val:
        val = sensor_val
        break
      else:
        print("error") 

      time.sleep(3)  
      continue

    return val

