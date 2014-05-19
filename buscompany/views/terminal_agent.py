from django.shortcuts import render
from buscompany.forms import VoyageLookupForm, TerminalAgentVoyageForm
from django.http import HttpResponseRedirect
from django.db import connection
import datetime
def getCityList():
	cursor = connection.cursor()
	cursor.execute(''' SELECT DISTINCT city FROM Terminal ORDER BY city ''')
	cities = zip(*(cursor.fetchall()))
	citylist = []
	for item in cities[0]:
		citylist.append((item,item,))
	return citylist
def dashboard(request):
	rows=[]
	cursor = connection.cursor()

	if request.method == 'POST':
		form = VoyageLookupForm(request.POST)
		citylist = getCityList()
		form.fields['departure_city'].choices=citylist
		form.fields['arrival_city'].choices=citylist
		if form.is_valid():
			

			cursor.execute('''SELECT r.route_id From Route r,Terminal t1,Terminal t2
							WHERE r.depart_terminal=t1.id AND t1.city=%s AND r.arrive_terminal=t2.id AND t2.city=%s''',
							[form.cleaned_data['departure_city'],form.cleaned_data['arrival_city']])

			route_id = cursor.fetchone()
			if route_id is not None:


				cursor.execute('''SELECT b.plate,v.departure_time,v.arrival_time,bt.model,v.id FROM Voyage v,Bus b,BusType bt
								 WHERE v.route_id=%s AND b.plate = v.plate AND bt.id=b.bustype_id
								 AND v.departure_time >= %s AND v.departure_time< %s''',
								 [route_id[0],form.cleaned_data['date'],form.cleaned_data['date']+datetime.timedelta(days=1)])

				rows=cursor.fetchall()
	else:
		form = VoyageLookupForm()
		citylist = getCityList()
		form.fields['departure_city'].choices=citylist
		form.fields['arrival_city'].choices=citylist

	
	return render(request,'terminal_agent/dashboard.html',{'lookupForm':form,'rows':rows})

def editVoyage(request,voyage_id):
	rows = []
	cursor = connection.cursor()
	cursor.execute(''' SELECT plate,departure_time,arrival_time FROM Voyage WHERE id=%s''',[voyage_id])
	row = cursor.fetchone()
	form = TerminalAgentVoyageForm()

	form.fields['departure_time'].initial=row[1]
	form.fields['arrival_time'].initial=row[2]
	if request.method == 'POST':
		form = TerminalAgentVoyageForm(request.POST)
		if form.is_valid():
			cursor.execute(''' UPDATE Voyage SET departure_time=%s, arrival_time=%s WHERE id=%s''',
				[form.cleaned_data['departure_time'],form.cleaned_data['arrival_time'],voyage_id])
	return render(request,'terminal_agent/editVoyage.html',{'form':form,'plate':row[0],'voyage_id':voyage_id})