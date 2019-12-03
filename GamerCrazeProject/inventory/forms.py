from django import forms

class SearchForm(forms.Form):
	quantity = forms.IntegerField();
	price = forms.DecimalField();
