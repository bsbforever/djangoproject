from django.contrib import admin

# Register your models here.
from navigation.models import serverinfo,path,addipaddress,oracleip,dy2018,cnbeta

admin.site.register(serverinfo)
admin.site.register(path)
admin.site.register(addipaddress)
admin.site.register(oracleip)
admin.site.register(dy2018)
admin.site.register(cnbeta)

