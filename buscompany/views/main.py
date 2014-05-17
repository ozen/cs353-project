from django.shortcuts import render
from buscompany.forms import VoyageLookupForm
from django.http import HttpResponseRedirect
from django.db import connection

def index(request):
	lookupForm = VoyageLookupForm()
	return render(request, 'main.html',{'lookupForm':lookupForm})


# an incomplete half-dummy implementation of listVoyages just to see how forms work
def listVoyages(request):
	if request.method == 'POST':
		form = VoyageLookupForm(request.POST)
		if form.is_valid():
			cursor = connection.cursor()
			#cursor.execute('''SELECT * FROM Terminal WHERE city='Ankara' ''')
			cursor.execute('''SELECT * From Route''')
			#	WHERE r.depart_terminal=t1.id AND t1.city=%s AND r.arrive_terminal=t2.id AND t2.city=%s',('Ankara','Istanbul'))
			
			row = cursor.fetchall()
			print row
			return render(request,'main.html',{'id':row})
	else:
		form = VoyageLookupForm()
	return render(request,'main.html',{'lookupForm':form})

