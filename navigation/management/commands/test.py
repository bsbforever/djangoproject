from django.core.management.base import BaseCommand       
from navigation.models import serverinfo,addipaddress
import os
from navigation.monitor.getinfo import *
class Command(BaseCommand):
    def handle(self, *args, **options):
        ip=['192.168.170.55']
        #ip=open(r'/root/ipaddress.txt','r')
        for ipaddress in ip:
            if getstatus(ipaddress)=='Online':
                diskcount=disktype(ipaddress)
                labelname=disklabel(ipaddress,diskcount)
                print labelname
                unitsize=diskunits(ipaddress,diskcount)
                disksize=disktotalsize(ipaddress,diskcount)
                print disksize
                diskused = diskusedsize(ipaddress,diskcount)
                print diskused
                memory=getmemory(ipaddress)
                print memory
                hostname=gethostname(ipaddress)
                print hostname
                status=getstatus(ipaddress)
                print status
                leng=len(diskcount)
                k=1
                for k in range(1, leng + 1):
                    totalspace=(float(unitsize[k-1][0]) * float(disksize[k-1][0]))/1024/1024/1024
                    print totalspace
                    #print 'The Total Size of  '+ labelname[k-1][0] +' Dirver on '+ipaddress+' is ' + str(totalspace)+' G'
                    freespace = (float(unitsize[k - 1][0]) * float(disksize[k - 1][0])) / 1024 / 1024 / 1024 - (float(unitsize[k - 1][0]) * float(diskused[k - 1][0])) / 1024 / 1024 / 1024
                    print freespace
                # print 'The Free Space of  '+ labelname[k-1][0] +' Dirver on '+ ipaddress+' is  ' + str(freespace)+' G'
                     #diskusage=float(totalspace-freespace)/float(totalspace)*100
                    #alertcontent='Be Careful, The Usage of '+ labelname[k-1][0]+' Driver on '+ipaddress+' is '+ str(diskusage)+' Used'
                #alert=result(ipaddress,diskcount,alert)
                    #info['ipaddress']=ipaddress
                    #labelname=labelname[k-1]
                    #info['totalspace']=int(totalspace)
                    if serverinfo.objects.filter(ip=ipaddress):
                        info=serverinfo.objects.filter(ip=ipaddress)
                        total=str(labelname[k-1])[2].lower()+'_total'
                        free=str(labelname[k-1])[2].lower()+'_free'
                        info.update(**{total:totalspace,free:freespace,'hostname':hostname,'memory':memory,'ifonline':status})
                    else:
                        createip=serverinfo(ip=ipaddress)
                        createip.save()
                        info=serverinfo.objects.filter(ip=ipaddress)
                        total=str(labelname[k-1])[2].lower()+'_total'
                        free=str(labelname[k-1])[2].lower()+'_free'
                        info.update(**{total:totalspace,free:freespace,'hostname':hostname,'memory':memory,'ifonline':status})
                        #info.update(**{total:totalspace,free:freespace})
            else:
                try:
                    info=serverinfo.objects.filter(ip=ipaddress)
                    info.update(**{'ifonline':'Offline'})
                except Exception ,e:
                    print e
