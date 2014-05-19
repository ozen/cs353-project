from django import forms
from buscompany.models import Bus

class VoyageLookupForm(forms.Form):
	departure_city = forms.CharField(max_length=100)
	arrival_city = forms.CharField(max_length=100)
	date = forms.DateField()

class BuyTicketForm(forms.Form):
	tck_no = forms.CharField(max_length=11)
	name = forms.CharField(max_length=35)
	surname = forms.CharField(max_length=15)
	date_of_birth = forms.DateField()
	num_of_tickets = forms.IntegerField()
	seat = forms.ChoiceField()
	gender = forms.ChoiceField(choices = [('m','Man'),('w','Woman')],widget=forms.RadioSelect())
	def __init__(self,ch):
		super(BuyTicketForm, self).__init__()
		self.fields['seat'].choices = [(2,3)]

class BusForm(forms.ModelForm):
	class Meta:
		model = Bus
		#fields = ['plate']
