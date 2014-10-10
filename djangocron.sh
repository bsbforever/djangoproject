#!/bin/sh 
cd /root/Django/mysite
PATH=$PATH:/usr/local/bin
export PATH
python manage.py getinfo    
