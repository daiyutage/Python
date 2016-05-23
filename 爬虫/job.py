#-*- coding:utf-8
#是否
import urllib
import urllib2
import re
import sys
import time
def replace(content):
    x = re.sub("&nbsp;"," ",content)
    return x
pageNum = 1
reload(sys)
sys.setdefaultencoding("utf8")
file = open("job.cvs","a+")
file.truncate()
count = 0
while(pageNum < 180):
    print "===================第"+str(pageNum)+"页====================="
    #file.writelines("===================第"+str(pageNum)+"页====================="+"\r\n")
    url = "http://jiuye.lut.cn/www/ContentsMain.asp?Page="+str(pageNum)+"&MainType=0&Keywords=&ClassId=27"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('gbk')

    pattern = re.compile('<td.*?style="line-height:24px;">.*?<span.*?blue">(.*?)</span>.*?<span.*?blue">(.*?)</span>.*?<span.*?blue">(.*?)</span>.*?</td>',re.S)
    items = re.findall(pattern,content)

    for item in items:
        print replace(item[0]),replace(item[1]),replace(item[2])
        count+=1

        file.writelines(replace(item[0])+",")
        file.writelines(replace(item[1])+",")
        file.write(replace(item[2]))
        file.write("\r\n")
    #print content
    time.sleep(1)
    pageNum+=1
