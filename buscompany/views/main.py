from django.shortcuts import render
from buscompany.forms import VoyageLookupForm
from django.http import HttpResponseRedirect
from django.db import connection

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
				cursor.execute('''SELECT v.departure_time,v.arrival_time,bt.model,v.occupied_seats,b.plate FROM Voyage v,Bus b,BusType bt
								 WHERE v.route_id=%s AND b.plate = v.plate AND bt.id=b.bustype_id
								 AND v.departure_time >= %s AND v.departure_time< "2014-06-02"''',
								 [route_id[0],form.cleaned_data['date']])

				rows=cursor.fetchall()
	else:
		form = VoyageLookupForm()
	return render(request,'common/list_voyages.html',{'lookupForm':form,'rows':rows})

