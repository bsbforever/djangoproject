# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
import MySQLdb
from navigation.models import path
from navigation.models import serverinfo
from navigation.models import dy2018
from navigation.models import cnbeta
from navigation.models import banyungong
# Create your views here.
from django.http import HttpResponse
from django import template
from form import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger     
from django.db.models.loading import get_model
# Create your views here。
def check_server(ipaddress,port):
    import socket
    s=socket.socket()
    try:
        s.connect((ipaddress,port))
        return True
    except socket.error,e:
        return False

def navigation (request):
    ipaddress=str(HttpResponse(request.META['REMOTE_ADDR'])).split('utf-8')[1].strip()
    result = path.objects.all().order_by('pathname')
    #pathname=result.pathname
    #path=result.path
    dic={'ipaddress':ipaddress,'result':result}    
    return render_to_response('navigation.html',dic)
    #return HttpResponse(result)
def getip(request):
	ipaddress=str(HttpResponse(request.META['REMOTE_ADDR'])).split('utf-8')[1].strip()
        return render_to_response('getip.html',{'ipaddress':ipaddress})
def scanport(request):
        return render_to_response('scanport.html')


def scanresult(request):
    try:
        ipaddress  = str(request.GET['ipaddress'])
        startport  = int(request.GET['startport'])
        endport  =   int(request.GET['endport'])
        if startport<=endport:
            ports=[]
            for i in range(startport,endport+1):
                ports.append(i)
            import socket
            openedport=[]
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for port in ports:
                check = check_server(ipaddress, port)
                if (check):
                    openedport.append(port)
                else: pass
            dic={'ipaddress':ipaddress,'openedport':openedport}
            return render_to_response('finalresult.html',dic)
        else:
            return HttpResponse('The Endport must greater than startport')
    except Exception,e:
        #return HttpResponse('Please Fill all the blanks below or enter right value')
        return HttpResponse(e)





def monitor(request):
    field_name=[]
    serverinfor=serverinfo.objects.all().order_by('ip')
    field_name=serverinfo._meta.get_all_field_names()
    dic={'serverinfor':serverinfor,'field_name':field_name}
    return render_to_response('monitor.html',dic)


def getsize(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = getpath(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            ipaddress=form.cleaned_data['ipaddress']
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            # Process the data in form.cleaned_data
            # ...
            return  HttpResponse(password)
            return HttpResponseRedirect('/navigation/') # Redirect after POST
    else:
        form = getpath() # An unbound form

    return render(request, 'getsize.html', {
        'form': form,
    })
def addcontent(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = addpath(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/navigation/') # Redirect after POST
    else:
        form = addpath() # An unbound form

    return render(request, 'addcontent.html', {
        'form': form,
    })

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/navigation/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    }) 

def scrapy(request):
    return render_to_response('scrapy.html')


def scrapy_dy2018(request):
    dy2018info=dy2018.objects.all().order_by('-id')
    formname='dy2018'
    paginator = Paginator(dy2018info, 75)
    page = request.GET.get('page')
    try:
        dy2018name = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dy2018name = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dy2018name = paginator.page(paginator.num_pages)
    dic={'formname':formname,'dy2018name':dy2018name}
    return render_to_response('scrapy_dy2018.html',dic)   

def scrapy_cnbeta(request):
    cnbetainfo=cnbeta.objects.all().order_by('-date')
    formname='cnbeta'
    paginator = Paginator(cnbetainfo, 75)
    page = request.GET.get('page')
    try:
        cnbetapage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cnbetapage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cnbetapage = paginator.page(paginator.num_pages)
    dic={'formname':formname,'cnbetapage':cnbetapage}
    return render_to_response('scrapy_cnbeta.html',dic)

def scrapy_banyungong(request):
    banyungonginfo=banyungong.objects.all().order_by('-id')
    formname='banyungong'
    paginator = Paginator(banyungonginfo, 75)
    page = request.GET.get('page')
    try:
        banyungongpage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        banyungongpage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        banyungongpage = paginator.page(paginator.num_pages)
    dic={'formname':formname,'banyungongpage':banyungongpage}
    return render_to_response('scrapy_banyungong.html',dic)

def search(request):
    formname=request.GET.get('formname')
    searchname=request.GET.get('searchname')
    search_column=request.GET.get('search_column')
    formname=get_model('navigation',formname)
    filter=search_column+'__contains'
    searchinfo=formname.objects.all().filter(**{filter:searchname}).order_by(search_column)
    return render_to_response('scrapy_search.html',{'searchinfo':searchinfo}) 
     
