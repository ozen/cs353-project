from django import forms
from buscompany.models import *

class VoyageLookupForm(forms.Form):
	departure_city = forms.ChoiceField()
	arrival_city = forms.ChoiceField()
	date = forms.DateField()

class BuyTicketForm(forms.Form):
    tck_no = forms.CharField(max_length=11)
    name = forms.CharField(max_length=35)
    surname = forms.CharField(max_length=15)
    date_of_birth = forms.DateField()
    seat = forms.ChoiceField()
    gender = forms.ChoiceField(choices = [('m','Man'),('w','Woman')],widget=forms.RadioSelect())

class BusForm(forms.ModelForm):
	class Meta:
		model = Bus

class BusTypeForm(forms.ModelForm):
    class Meta:
        model = BusType

class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route

class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage

class TerminalAgentVoyageForm(forms.Form):
	departure_time = forms.DateTimeField(label='Departure Time')
	arrival_time = forms.DateTimeField(label='Arrival Time')
