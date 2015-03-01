from django.conf.urls import patterns, include, url
from django.contrib import admin
import prueba
from prueba.views import current_datetime,hours_ahead

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^time/$', include('prueba.urls')),
    #url(r'^time/$', curent_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
