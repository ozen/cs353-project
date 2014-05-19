from django import forms

class VoyageLookupForm(forms.Form):
	departure_city = forms.CharField(max_length=100)
	arrival_city = forms.CharField(max_length=100)
	date = forms.DateField()

class BuyTicketForm(forms.Form):
	tck_no = forms.CharField(max_length=11)
	name = forms.CharField(max_length=35)
	surname = forms.CharField(max_length=15)
	date_of_birth = forms.DateField()
	seat = forms.ChoiceField()
	gender = forms.ChoiceField(choices = [('m','Man'),('w','Woman')],widget=forms.RadioSelect())
