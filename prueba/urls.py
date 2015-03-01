__author__ = 'daniel'
from prueba.views import curent_datetime
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', curent_datetime, name='current_datetime'),

)


