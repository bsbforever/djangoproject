from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
   # url(r'^$', views.index, name='index')
   #   url(r'^$', name='index')
     url(r'^$', views.index, name='index'),
     url(r'^search-form/', views.search_form, name='search_form'),
     url(r'^search/', views.search, name='search'),
     url(r'^test/', views.test, name='test'),
     url(r'^ip/', views.ip, name='ip')
)

