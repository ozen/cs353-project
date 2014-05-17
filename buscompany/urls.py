from django.conf.urls import patterns, url
from buscompany import views

urlpatterns = [
    url(r'^$', views.main.index),
    url(r'^manager/$', views.manager.dashboard),
    url(r'^salesperson/$', views.salesperson.dashboard),
    url(r'^terminal_agent/$', views.terminal_agent.dashboard),
    url(r'^listVoyages/$', views.main.listVoyages),
]
