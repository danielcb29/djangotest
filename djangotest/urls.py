from django.conf.urls import patterns, include, url
from django.contrib import admin
import prueba
from prueba.views import current_datetime,hours_ahead
from books.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^time/', include('prueba.urls')),

    url(r'^search/',include('books.urls')),

    url(r'^contact/$',contact),

    url(r'^contact/thanks$',thanks),

    url(r'^meta/$',display_meta),
    url(r'^dcbook/$',show_dcbook)
)
