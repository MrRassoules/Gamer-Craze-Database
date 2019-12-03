from django import forms 
from inventory.models import *

class SearchForm(forms.Form):
	card_name = forms.CharField(max_length = 30, widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	price = forms.DecimalField(decimal_places = 2)
	