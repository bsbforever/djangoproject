from django.core.management.base import BaseCommand
from navigation.models import serverinfo,addipaddress
import os
from navigation.monitor.getoracleinfo import *
class Command(BaseCommand):
    def handle(self, *args, **options):
        ipaddress='192.168.173.3'
        username='sajet'
        password='tech'
        port='1521'
        tnsname='TSH1'
        db = cx_Oracle.connect(username+'/'+password+'@'+ ipaddress+':'+ port +'/'+tnsname)
        version= db.version
        cursor = db.cursor()
        dbname=getdbname(cursor)
        instancename=getinstancename(cursor)
        result=checkifrac(cursor)
        cursor.close()
        db.close()
        print result       
