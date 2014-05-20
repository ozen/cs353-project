from django.conf.urls import patterns, url
from buscompany import views

urlpatterns = [
    url(r'^$', views.main.index),
    url(r'^manager/$', views.manager.dashboard),
    url(r'^manager/addBus/((?P<plate>.+)/)?$', views.manager.addBus),
    url(r'^manager/addBusType/((?P<pk>\d+)/)?$', views.manager.addBusType),
    url(r'^manager/addGarage/((?P<pk>\d+)/)?$', views.manager.addGarage),
    url(r'^manager/addRoute/((?P<pk>\d+)/)?$', views.manager.addRoute),
    url(r'^manager/addVoyage/((?P<pk>\d+)/)?$', views.manager.addVoyage),
    url(r'^manager/listBus$', views.manager.listBus),
    url(r'^manager/listBusType$', views.manager.listBusType),
    url(r'^manager/listGarage$', views.manager.listGarage),
    url(r'^manager/listRoute$', views.manager.listRoute),
    url(r'^manager/listVoyage$', views.manager.listVoyage),
    url(r'^manager/deleteBus/(?P<plate>.+)/$', views.manager.deleteBus),
    url(r'^manager/deleteBusType/(?P<pk>\d+)/$', views.manager.deleteBusType),
    url(r'^manager/deleteGarage/(?P<pk>\d+)/$', views.manager.deleteGarage),
    url(r'^manager/deleteRoute/(?P<pk>\d+)/$', views.manager.deleteRoute),
    url(r'^manager/deleteVoyage/(?P<pk>\d+)/$', views.manager.deleteVoyage),
    url(r'^manager/report/([0-9])/$', views.manager.report),
    url(r'^salesperson/$', views.salesperson.dashboard),
    url(r'^salesperson/tickets/$', views.salesperson.tickets),
    url(r'^salesperson/cancelTicket/([0-9]+)/$', views.salesperson.cancelTicket),
    url(r'^salesperson/reservations/$', views.salesperson.reservations),
    url(r'^terminal_agent/$', views.terminal_agent.dashboard),
    url(r'^terminal_agent/editVoyage/([0-9]+)/$', views.terminal_agent.editVoyage),
    url(r'^listVoyages/$', views.main.listVoyages),
    url(r'^buyTicket/([0-9]+)/$', views.main.buyTicket),
    url(r'^makeReservation/([0-9]+)/$', views.main.makeReservation),
    url(r'^ticketDetails/([0-9]+)/$', views.salesperson.ticketDetails),
    url(r'^reservationDetails/([0-9]+)/$', views.salesperson.reservationDetails),
    url(r'^salesperson/cancelReservation/([0-9]+)/$', views.salesperson.cancelReservation),
]

