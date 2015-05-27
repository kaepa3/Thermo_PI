
# -*- coding: utf-8 -*-
import urllib
import urllib2
from datetime import datetime

class CommitDataClass(object):
  """docCommit_Data_Classme"""
  url = 'http://localhost:3000/heya/create'
      
  def send_data(self, ondo, shitudo):
    params = {'temperature' : str(ondo), 'humidity' : str(shitudo), \
                'date': datetime.now().strftime('%Y/%m/%d %H:%M:%S') }
    print params
    params = urllib.urlencode(params)
    req = urllib2.Request(self.url)
    print self.url
    # ヘッダ追加
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    # パラメータ追加 
    req.add_data(params)

    urllib2.urlopen(req)

if __name__ == '__main__':
    obj = CommitDataClass()
    obj.send_data(20, 20)


