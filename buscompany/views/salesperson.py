from django.shortcuts import render
from buscompany.forms import VoyageLookupForm,BuyTicketForm,SearchTicketForm
from buscompany.views.main import *
from django.http import HttpResponseRedirect
from django.db import connection
import datetime
from buscompany.views.main import createListVoyages


def dashboard(request):
	form,rows = createListVoyages(request)
	return render(request,'salesperson/dashboard.html',{'lookupForm':form,'rows':rows})
def tickets(request):
	rows=[]
	cursor = connection.cursor()
	if request.method == 'POST':
		form = SearchTicketForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['tck_no']:
				cursor.execute(''' SELECT c.name,c.surname,t.voyage_id,t.payment_time FROM Ticket t, Customer c WHERE t.tck_no=%s AND t.tck_no=c.tck_no ORDER BY payment_time''',[form.cleaned_data['tck_no']])
				rows=cursor.fetchall()
			elif form.cleaned_data['surname'] and form.cleaned_data['name']:
				query = ''' SELECT c.name,c.surname,t.voyage_id,t.payment_time FROM Ticket t,Customer c
					WHERE c.tck_no=t.tck_no AND c.surname LIKE '''
				query = query + "'%" + form.cleaned_data['surname'] + "%' AND c.name LIKE '%" + form.cleaned_data['name'] + "%' ORDER BY t.payment_time"
				cursor.execute(query)
				rows=cursor.fetchall()
			elif form.cleaned_data['surname']:
				query = ''' SELECT c.name,c.surname,t.voyage_id,t.payment_time FROM Ticket t,Customer c
					WHERE c.tck_no=t.tck_no AND c.surname LIKE '''
				query =query + "'%" + form.cleaned_data['surname'] + "%' ORDER BY t.payment_time"
				cursor.execute(query)
				rows=cursor.fetchall()
			elif form.cleaned_data['name']:
				query = ''' SELECT c.name,c.surname,t.voyage_id,t.payment_time FROM Ticket t,Customer c
					WHERE c.tck_no=t.tck_no AND c.name LIKE '''
				query =query + "'%" + form.cleaned_data['name'] + "%' ORDER BY t.payment_time"
				cursor.execute(query)
				rows=cursor.fetchall()
			else:
				rows = []		

	else:
		form = SearchTicketForm()
	return render(request,'salesperson/see_tickets.html',{'form':form,'rows':rows})
def ticketDetails(request,ticket_id):
	rows=[]
	cursor = connection.cursor()
	cursor.execute('''SELECT v.route_id,v.departure_time FROM Voyage v,Ticket t WHERE t.voyage_id=v.id AND t.id=%s''',[ticket_id])
	v = cursor.fetchone()
	cursor.execute('''SELECT t1.city,t2.city FROM ROUTE r,Terminal t1,Terminal t2 WHERE r.depart_terminal=t1.id AND
		r.arrive_terminal=t2.id AND r.route_id=%s''',[v[0]])
	yol =cursor.fetchone()
	v=zip(v)
	yol=zip(yol)
	tt =v +yol
	for item in tt:
		rows.append(item[0])

	return render(request,'common/ticketDetails.html',{'rows':rows})
def cancelTicket(request,ticket_id):
	rows=[]
	cursor = connection.cursor()
	cursor.execute(''' DELETE FROM Ticket WHERE id=%s''',[ticket_id])

	return render(request,'salesperson/deleted.html',{'rows':rows})
def reservations(request):
	rows=[]
	cursor = connection.cursor()
	if request.method == 'POST':
		form = SearchTicketForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['tck_no']:
				cursor.execute(''' SELECT c.name,c.surname,t.voyage_id,t.time FROM Reservation t, Customer c WHERE t.tck_no=%s AND t.tck_no=c.tck_no ORDER BY time''',[form.cleaned_data['tck_no']])
				rows=cursor.fetchall()
			elif form.cleaned_data['surname'] and form.cleaned_data['name']:
				query = ''' SELECT c.name,c.surname,t.voyage_id,t.time FROM Reservation t,Customer c
					WHERE c.tck_no=t.tck_no AND c.surname LIKE '''
				query = query + "'%" + form.cleaned_data['surname'] + "%' AND c.name LIKE '%" + form.cleaned_data['name'] + "%' ORDER BY t.time"
				cursor.execute(query)
				rows=cursor.fetchall()
			elif form.cleaned_data['surname']:
				query = ''' SELECT c.name,c.surname,t.voyage_id,t.time FROM Reservation t,Customer c
					WHERE c.tck_no=t.tck_no AND c.surname LIKE '''
				query =query + "'%" + form.cleaned_data['surname'] + "%' ORDER BY t.time"
				cursor.execute(query)
				rows=cursor.fetchall()
			elif form.cleaned_data['name']:
				query = ''' SELECT c.name,c.surname,t.voyage_id,t.time FROM Reservation t,Customer c
					WHERE c.tck_no=t.tck_no AND c.name LIKE '''
				query =query + "'%" + form.cleaned_data['name'] + "%' ORDER BY t.time"
				cursor.execute(query)
				rows=cursor.fetchall()
			else:
				rows = []		

	else:
		form = SearchTicketForm()
	return render(request,'salesperson/see_reservations.html',{'form':form,'rows':rows})

def reservationDetails(request,ticket_id):
	rows=[]
	cursor = connection.cursor()
	cursor.execute('''SELECT v.route_id,v.departure_time FROM Voyage v,Reservation t WHERE t.voyage_id=v.id AND t.id=%s''',[ticket_id])
	v = cursor.fetchone()
	cursor.execute('''SELECT t1.city,t2.city FROM ROUTE r,Terminal t1,Terminal t2 WHERE r.depart_terminal=t1.id AND
		r.arrive_terminal=t2.id AND r.route_id=%s''',[v[0]])
	yol =cursor.fetchone()
	v=zip(v)
	yol=zip(yol)
	tt =v +yol
	for item in tt:
		rows.append(item[0])
	return render(request,'salesperson/reservation_details.html',{'rows':rows})

def cancelReservation(request,ticket_id):
	rows=[]
	cursor = connection.cursor()
	cursor.execute(''' DELETE FROM Reservation WHERE id=%s''',[ticket_id])

	return render(request,'salesperson/deleted.html',{'rows':rows})