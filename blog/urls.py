from django.conf.urls import *

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.EntryIndex.as_view(), name='bloghome'),
    url((r'^(?P<year>\d{4})/'
          '(?P<month>\d{1,2})/'
          '(?P<day>\d{1,2})/'
          '(?P<pk>\d+)-(?P<slug>[-\w]*)/$'), 
        views.EntryDetail.as_view(), 
        name='entry_detail'),
    url(r'^tag/(?P<slug>[-\w+]+)/$', 
        views.TagIndexView.as_view(), name='tagged'),
)
