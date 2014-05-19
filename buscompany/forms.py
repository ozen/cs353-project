from django import forms
from buscompany.models import *
from django.utils.translation import ugettext_lazy as _

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
        labels = {
            'bustype_id': _('Bus Type'),
        }

class BusTypeForm(forms.ModelForm):
    class Meta:
        model = BusType

class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        exclude = ['route_id']

class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        labels = {
            'route_id': _('Route'),
        }

class TerminalAgentVoyageForm(forms.Form):
	departure_time = forms.DateTimeField(label='Departure Time')
	arrival_time = forms.DateTimeField(label='Arrival Time')

class SearchTicketForm(forms.Form):
	tck_no = forms.CharField(max_length=11,required=False)
	name = forms.CharField(max_length=35,required=False)
	surname = forms.CharField(max_length=15,required=False)
