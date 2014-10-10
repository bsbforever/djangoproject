# -*-coding:utf-8 -*-
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
import re
from monitor.getinfo import *
import models
result =models. path.objects.all().order_by('pathname')
for i in result:
    print i
#print result
def getspace():
    ip=open(r'/root/ipaddress.txt','r')
    info={}
    result=[]
    alert=''
    for ipaddress in ip:
        ipaddress=ipaddress.strip()
        diskcount=disktype(ipaddress)
        labelname=disklabel(ipaddress,diskcount)
        unitsize=diskunits(ipaddress,diskcount)
        disksize=disktotalsize(ipaddress,diskcount)
        diskused = diskusedsize(ipaddress,diskcount)
        diskfailures=diskfailuresnum(ipaddress,diskcount)
        leng=len(diskcount)
        k=1
        for k in range(1, leng + 1):
            totalspace=(int(unitsize[k-1][0]) * int(disksize[k-1][0]))/1024/1024/1024
            print 'The Total Size of  '+ labelname[k-1][0] +' Dirver on '+ipaddress+' is ' + str(totalspace)+' G'
            freespace = (int(unitsize[k - 1][0]) * int(disksize[k - 1][0])) / 1024 / 1024 / 1024 - (int(unitsize[k - 1][0]) * int(diskused[k - 1][0])) / 1024 / 1024 / 1024
           # print 'The Free Space of  '+ labelname[k-1][0] +' Dirver on '+ ipaddress+' is  ' + str(freespace)+' G'
            #diskusage=float(totalspace-freespace)/float(totalspace)*100
            #alertcontent='Be Careful, The Usage of '+ labelname[k-1][0]+' Driver on '+ipaddress+' is '+ str(diskusage)+' Used'
        #alert=result(ipaddress,diskcount,alert)
            info['ipaddress']=ipaddress
            info['labelname']=labelname[k-1]
            info['totalspace']=int(totalspace)
            info['freespace']=int(freespace)
            result.append({'ipaddress':ipaddress,'labelname':labelname[k-1],'totalspace':int(totalspace),'freespace':int(freespace)})

getspace()
