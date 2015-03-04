__author__ = 'daniel'
from books.views import *
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',search , name='search'),
    #url(r'^plus/(\d{1,2})/$', hours_ahead),
    url(r'^english/$',search_new,name='new search'), # example for english book


)