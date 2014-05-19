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


				cursor.execute('''SELECT v.departure_time,v.arrival_time,bt.model,v.occupied_seats,v.id,b.plate FROM Voyage v,Bus b,BusType bt
								 WHERE v.route_id=%s AND b.plate = v.plate AND bt.id=b.bustype_id
								 AND v.departure_time >= %s AND v.departure_time< %s''',
								 [route_id[0],form.cleaned_data['date'],form.cleaned_data['date']+datetime.timedelta(days=1)])

				rows=cursor.fetchall()
	else:
		form = VoyageLookupForm()
	return render(request,'common/list_voyages.html',{'lookupForm':form,'rows':rows})

def buyTicket(request,voyage_id):
	cursor = connection.cursor()
	cursor.execute('''SELECT seat FROM Ticket WHERE voyage_id=%s ''',[voyage_id])
	occupied_seats = cursor.fetchall()
	if occupied_seats:
		occupied_seats = map(list, zip(*occupied_seats))[0]#zip(*occupied_seats)
	else:
		occupied_seats = []
	cursor.execute('''SELECT bt.passenger_capacity FROM Voyage v,Bus b,BusType bt 
		WHERE v.id=%s AND v.plate=b.plate AND b.bustype_id=bt.id ''',[voyage_id])
	passenger_capacity = cursor.fetchall()[0]
	passenger_capacity = passenger_capacity[0]
	
	unoccupied_seats_list = []
	for i in range(1,passenger_capacity+1):
		if i not in occupied_seats:
			unoccupied_seats_list.append((i,i,))

	if request.method == 'POST':

		form = BuyTicketForm(request.POST)
		form.fields['seat'].choices = unoccupied_seats_list

		if form.is_valid():
			cursor = connection.cursor()
			price = 1
			cursor.execute(''' SELECT * FROM Customer WHERE tck_no = %s''',[request.POST['tck_no']])
			if not cursor.fetchone():
				cursor.execute('''INSERT INTO Customer VALUES(%s,%s,%s,%s,%s) ''',[form.cleaned_data['tck_no'],
					form.cleaned_data['name'],form.cleaned_data['surname'],form.cleaned_data['date_of_birth'],
					form.cleaned_data['gender']])

				
			cursor.execute('''SELECT price,plate FROM Voyage WHERE id=%s ''',[voyage_id])
			row = cursor.fetchone()
			price = row[0]
			cursor.execute(''' INSERT INTO Ticket(tck_no,voyage_id,seat,payment_type,payment_time,price) VALUES(%s,%s,%s,%s,%s,%s)''',[form.cleaned_data['tck_no'],
				voyage_id,form.cleaned_data['seat'],'creditcard',datetime.datetime.now(),price])

			cursor.execute(''' SELECT t1.city,t2.city,v.departure_time From Route r,Terminal t1,Terminal t2,Voyage v
							WHERE r.depart_terminal=t1.id AND r.arrive_terminal=t2.id 
							AND v.id=%s AND v.route_id=r.route_id''',[voyage_id])
			row = cursor.fetchone()
			fr = row[0]
			to = row[1]
			dtime = row[2]
			return render(request,'common/ticketDetail.html',{'fr':fr,'to':to,'dtime':dtime,'seat':form.cleaned_data['seat']})
	else:

		
		form = BuyTicketForm()
		form.fields['seat'].choices = unoccupied_seats_list

	return render(request,'common/buyTicketForm.html',{'voyage_id':voyage_id,'buyForm':form})

