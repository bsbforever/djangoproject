# coding:utf8
from django.db import models
from django import forms
#os.environ['DJANGO_SETTINGS_MODULE'] ='mysite.settings'


# Create your models here.

class serverinfo(models.Model):
    ip=models.GenericIPAddressField(primary_key=True)
    hostname=models.CharField(max_length=100,blank=True,null=True)
    memory=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    c_total=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    c_free=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    c_usage=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    d_total=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    d_free=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    d_usage=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    e_total=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    e_free=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    e_usage=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    f_total=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    f_free=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    f_usage=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    g_total=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    g_free=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    g_usage=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    h_total=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    h_free=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    h_usage=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    i_total=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    i_free=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    i_usage=models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    ifonline=models.CharField(max_length=10,blank=True,null=True)
    def __unicode__(self):
       return self.ip
    class Meta:
        app_label='navigation'

class path(models.Model):
    pathname=models.CharField(max_length=30,primary_key=True)
    path=models.CharField(max_length=300)
    def __unicode__(self):
        return u'%s,%s' %(self.pathname,self.path)
    class Meta:
        app_label='navigation'



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class addipaddress(models.Model):
    ipaddress=models.GenericIPAddressField(primary_key=True)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='navigation'


class oracleip(models.Model):
    ipaddress=models.GenericIPAddressField(primary_key=True)
    username=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    port=models.CharField(max_length=300)
    tnsname=models.CharField(max_length=300)
    hostname=models.CharField(max_length=300)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='navigation'




class dy2018(models.Model):
    type=models.CharField(max_length=300)
    title=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    def __unicode__(self):
        return self.type
    class Meta:
        app_label='navigation'

class cnbeta(models.Model):
    date=models.CharField(max_length=300)
    title=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    def __unicode__(self):
        return self.title
    class Meta:
        app_label='navigation'



class banyungong(models.Model):
    title=models.CharField(max_length=300)
    type=models.CharField(max_length=300)
    link=models.CharField(max_length=300)
    def __unicode__(self):
        return self.title
    class Meta:
        app_label='navigation'

