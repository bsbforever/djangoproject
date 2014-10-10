from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'navigation.views.navigation', name='navigation'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^navigation/', include('navigation.urls')),
   # url(r'^$', 'polls.views.index', name='index')
)

