from django.conf.urls import patterns, include, url
from django.contrib import admin

import blog.urls
from . import views

urlpatterns = [
#    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(blog.urls)),
]
