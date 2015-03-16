
# -*- coding: utf-8 -*-
import dhtreader_class
import commit_fata_class

type = 11
pin =26

reader = DhtReader_Class(type,pin)
if True == reader.init_devise:
   print reader.read_value


