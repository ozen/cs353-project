from django import forms

class VoyageLookupForm(forms.Form):
	departure_city = forms.CharField(max_length=100)
	arrival_city = forms.CharField(max_length=100)
	date = forms.DateField()