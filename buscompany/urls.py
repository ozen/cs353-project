from django.conf.urls import patterns, url
from buscompany import views

urlpatterns = [
    url(r'^$', views.main.index),
    url(r'^manager/$', views.manager.dashboard),
    url(r'^listVoyages/$', views.main.listVoyages),
]
