from django.conf.urls import patterns, url
from buscompany import views

urlpatterns = [
    url(r'^$', views.main.index),
    url(r'^manager/$', views.manager.dashboard),
    url(r'^manager/addBus$', views.manager.addBus),
    url(r'^manager/addBusType$', views.manager.addBusType),
    url(r'^manager/addGarage$', views.manager.addGarage),
    url(r'^manager/addRoute$', views.manager.addRoute),
    url(r'^manager/addVoyage$', views.manager.addVoyage),
    url(r'^manager/listBus$', views.manager.listBus),
    url(r'^manager/listBusType$', views.manager.listBusType),
    url(r'^manager/listGarage$', views.manager.listGarage),
    url(r'^manager/listRoute$', views.manager.listRoute),
    url(r'^manager/listVoyage$', views.manager.listVoyage),
    url(r'^salesperson/$', views.salesperson.dashboard),
    url(r'^terminal_agent/$', views.terminal_agent.dashboard),
    url(r'^listVoyages/$', views.main.listVoyages),
    url(r'^buyTicket/([0-9]+)/$', views.main.buyTicket),
    url(r'^makeReservation/([0-9]+)/$', views.main.makeReservation),
]
