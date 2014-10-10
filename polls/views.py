from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from django import template
def index(request):
     import socket
     ipaddress=str(HttpResponse(request.META['REMOTE_ADDR'])).split('utf-8')[1].strip()
     ipaddress2=str(HttpResponse(request.META['REMOTE_ADDR']))
     dic={'ipaddress':ipaddress,'ipaddress2':ipaddress2}
     return render_to_response('index.html',dic)
def test(request):
	ipaddress=str(HttpResponse(request.META['REMOTE_ADDR'])).split('utf-8')[1].strip()
	ipaddress2=str(HttpResponse(request.META['REMOTE_ADDR']))
        dic={'ipaddress':ipaddress,'ipaddress2':ipaddress2}
        return render_to_response('test.html',dic)
def ip(request):
	ipaddress= str(HttpResponse(request.is_secure() ))
	#ipaddress=str(HttpResponse(request.META['REMOTE_ADDR'])).split('utf-8')[1].strip()
        return render_to_response('ip.html',{'ipaddress':ipaddress})
def search_form(request):
	return render_to_response('search_form.html')
def search(request):
	if 'q' in request.GET:
		message = 'You searched for: %r' % request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)
