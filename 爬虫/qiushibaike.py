# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
import os

os.remove('xiaohua.txt')
page = 2
while(page<20):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
      #  print content
        pattern = re.compile('<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>',re.S)
        items = re.findall(pattern,content)
        reload(sys)
        sys.setdefaultencoding("utf8")
        file = open('xiaohua.txt','a+')
        for item in items:
            print item[0]
            print item[1]


    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    print page,"======================================================================================================"
    break
    page = page+1
