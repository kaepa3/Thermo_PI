
# -*- coding: utf-8 -*-
import dhtreader_class
import commitdataclass


type = 11
pin =26

reader = DhtReader_Class(type,pin)
if True == reader.init_devise:
  val = reader.read_value
  if val != None:
    obj = CommitDataClass()
    obj.send_data(val.first, val.last)


