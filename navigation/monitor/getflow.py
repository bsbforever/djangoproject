import re
import os
def getcount(ipaddress):
    count=[]
    j=1
    fp1=os.popen('snmpwalk -v 2c -c public '+ ipaddress +' ifType')
    for i in fp1:
        if 'ethernetCsmacd' in i:
            count.append(j)
            j=j+1
        else:
            j=j+1
    fp1.close()
    return count


if __name__ == '__main__':
    ipaddress='192.168.173.201'
    count=getcount(ipaddress)
    print count
