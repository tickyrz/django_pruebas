from django.conf.urls import patterns, url, include
from mysite.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'admin/', include(admin.site.urls)),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)