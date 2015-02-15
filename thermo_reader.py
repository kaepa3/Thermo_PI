
# -*- coding: utf-8 -*-
import dhtreader

type = 11
pin = 7


dhtreader.init()
print dhtreader.read(type, pin)
