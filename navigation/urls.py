from django.conf.urls import patterns, url

from navigation  import views

urlpatterns = patterns('',
   # url(r'^$', views.index, name='index')
   #   url(r'^$', name='index')
     url(r'^$',views.navigation, name='navigation'),
     url(r'^getip/$',views.getip, name='getip'),
     url(r'^scanport/$',views.scanport, name='scanport'),
     url(r'^scanresult/$',views.scanresult, name='scanresult'),
     url(r'^monitor/$',views.monitor, name='monitor'),
     url(r'^search/$',views.search, name='search'),
     url(r'^addcontent/$',views.addcontent, name='addcontent'),
     url(r'^getsize/$',views.getsize, name='getsize'),
     url(r'^contact/$',views.contact, name='contact'),
     #url(r'^thanks/$',views.thanks, name='thanks'),
    #   url(r'^finalresult/$',views.finalresult, name='finalresult'),
     # url(r'^$',views.navigation, name='navigation'),
)

     



urlpatterns += patterns('',
    url(r'^scrapy/$',views.scrapy, name='scrapy'),
    url(r'^scrapy/dy2018/$',views.scrapy_dy2018, name='scrapy_dy2018'),
    url(r'^scrapy/cnbeta/$',views.scrapy_cnbeta, name='scrapy_cnbeta'),
    url(r'^scrapy/banyungong/$',views.scrapy_banyungong, name='scrapy_banyungong'),

)




