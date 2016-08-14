import django
from django.conf.urls import url,include
from django.contrib import admin

import  views
from  usercenter.views import activate

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/', include('article.urls')),
    url(r'^register/',views.register),
    url(r'^activate/(?P<code>\w+)/$', activate),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$',views.index),
]