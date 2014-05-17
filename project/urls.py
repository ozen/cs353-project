from django.conf.urls import patterns, include, url
from buscompany import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^listVoyages/$', views.main.listVoyages),
    url(r'^$', views.main.index)
)
