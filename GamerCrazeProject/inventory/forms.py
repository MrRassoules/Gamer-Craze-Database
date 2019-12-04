from django import forms
from inventory.models import *

class SearchForm(forms.Form):
	RARITY_CHOICES = (
		('', '------'),
        ('B', 'Basic'),
        ('C', 'Common'),
        ('U', 'Uncommon'),
        ('R', 'Rare'),
        ('M', 'Mythic Rare')
    )

	card_name = forms.CharField(required = False, max_length = 30, widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	rule_text = forms.CharField(required = False, max_length = 400)
	rarity = forms.ChoiceField(required = False, choices = RARITY_CHOICES)
