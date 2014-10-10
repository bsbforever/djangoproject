import re
import os
import cx_Oracle
def getdbname(cursor):
    '''db = cx_Oracle.connect(username+'/'+password+'@'+ ipaddress+':'+'/'+tnsname)
    cursor = db.cursor()'''
    cursor.execute('select name from v$database')
    row=cursor.fetchone()
    dbname=row[0]
    return dbname

def getinstancename(cursor):
    cursor.execute('select instance_name from v$instance')
    row=cursor.fetchone()
    instancename=row[0]
    return instancename

def checkifrac(cursor):
    cursor.execute('select value from v$option where  parameter=\'Real Application Clusters\'')
    row=cursor.fetchone()
    result=row[0]
    return result

def checkram(cursor):
        cursor.execute('select status from v$rman_backup_job_details')
        row=cursor.fetchall()
        j=1
        try:
            for i in row:
                if j==30:
                    ram=i[0]
                    break
                else:
                    j=j+1
            return ram
        except:
            return 'None'            

def getspace(cursor):
    fp=open('/root/Django/mysite/navigation/monitor/tablespacesize.sql','r') 
    fp=fp.read()
    s=cursor.execute(fp)
    row=s.fetchall()
    return row

if __name__ == '__main__':
    ipaddress='192.168.173.3'
    username='sajet'
    password='tech'
    port='1521'
    tnsname='TSH1'
    db = cx_Oracle.connect(username+'/'+password+'@'+ ipaddress+':'+'/'+tnsname)
    cursor = db.cursor()
    s=getspace(cursor)
    for i in s:
        print i[0],i[1],i[4]
    cursor.close()
    db.close()
    
