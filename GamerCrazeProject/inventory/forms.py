from django import forms
from inventory.models import *

class SearchForm(forms.Form):
	card_name = forms.CharField(required = False, max_length = 30, widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	rule_text = forms.CharField(required = False, max_length = 400)
