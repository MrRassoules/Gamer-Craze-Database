from django import forms

class ManageCardsForm(forms.Form):
	quantity = forms.IntegerField();
	price = forms.DecimalField();
	

