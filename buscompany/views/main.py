from django.shortcuts import render
from buscompany.forms import VoyageLookupForm,BuyTicketForm
from django.http import HttpResponseRedirect
from django.db import connection
import datetime

def index(request):
	return render(request, 'frontpage.html')


# an incomplete half-dummy implementation of listVoyages just to see how forms work
def listVoyages(request):
	rows=[]
	if request.method == 'POST':
		form = VoyageLookupForm(request.POST)
		if form.is_valid():
			cursor = connection.cursor()

			cursor.execute('''SELECT r.route_id From Route r,Terminal t1,Terminal t2
							WHERE r.depart_terminal=t1.id AND t1.city=%s AND r.arrive_terminal=t2.id AND t2.city=%s''',
							[form.cleaned_data['departure_city'],form.cleaned_data['arrival_city']])

			route_id = cursor.fetchone()
			if route_id is not None:

				#date hardcoded in sql statement. FIX THIS!!!
				cursor.execute('''SELECT v.departure_time,v.arrival_time,bt.model,v.occupied_seats,v.id,b.plate FROM Voyage v,Bus b,BusType bt
								 WHERE v.route_id=%s AND b.plate = v.plate AND bt.id=b.bustype_id
								 AND v.departure_time >= %s AND v.departure_time< "2014-06-02"''',
								 [route_id[0],form.cleaned_data['date']])

				rows=cursor.fetchall()
	else:
		form = VoyageLookupForm()
	return render(request,'common/list_voyages.html',{'lookupForm':form,'rows':rows})

def buyTicket(request,voyage_id):
	if request.method == 'POST':
		form = BuyTicketForm(request.POST)
		if form.is_valid():
			cursor = connection.cursor()

			cursor.execute(''' SELECT * FROM Customer WHERE tck_no = %s''',[form.cleaned_data['tck_no']])
			if not cursor.fetchone():
				cursor.execute('''INSERT INTO Customer VALUES(%s,%s,%s,%s,%s) ''',[form.cleaned_data['tck_no'],
					form.cleaned_data['name'],form.cleaned_data['surname'],form.cleaned_data['date_of_birth'],
					form.cleaned_data['gender']])

			cursor.execute('''SELECT price,plate FROM Voyage WHERE id=%s ''',[voyage_id])
			row = cursor.fetchone()
			price = row[0]
			plate = row[1]


			cursor.execute(''' INSERT INTO Ticket(tck_no,voyage_id,seat,payment_type,payment_time,price) VALUES(%s,%s,%s,%s,%s,%s)''',[form.cleaned_data['tck_no'],
				voyage_id,seat,'creditcard',datetime.datetime.now(),price])


		
	else:
		cursor = connection.cursor()
		cursor.execute('''SELECT seat FROM Ticket WHERE voyage_id=%s ''',[voyage_id])
		occupied_seats = cursor.fetchall()
		cursor.execute('''SELECT bt.passenger_capacity FROM Voyage v,Bus b,BusType bt 
			WHERE v.id=%s AND v.plate=b.plate AND b.bustype_id=bt.id ''',[voyage_id])
		passenger_capacity = cursor.fetchall()
		 
		form = BuyTicketForm(('d'))

	return render(request,'common/buyTicketForm.html',{'voyage_id':voyage_id,'buyForm':form,'occupied_seats':occupied_seats,'passenger_capacity':passenger_capacity})

