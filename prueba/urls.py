__author__ = 'daniel'
from prueba.views import current_datetime,hours_ahead
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', current_datetime, name='current_datetime'),
    url(r'^plus/(\d{1,2})/$', hours_ahead),

)


