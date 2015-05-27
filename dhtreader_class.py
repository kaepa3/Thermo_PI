
# -*- coding: utf-8 -*-
import dhtreader
import os
import time

class DhtReader_Class:
  def __init__ (self, device_type , pin_no):
    self.type  = device_type
    self.pin   = pin_no

  def init_devise(self):
    if 0 != dhtreader.init():

      return True
    print("init error")
    return False

  def read_value(self):
    val = None
    for _ in range(10):
      sensor_val = dhtreader.read(self.type, self.pin)
      if sensor_val:
        val = sensor_val
        break

      time.sleep(3)  
      continue

    return val

