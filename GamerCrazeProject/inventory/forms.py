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

	COLOR_CHOICES = (
		('', '------'),
        ('W', 'White'),
        ('U', 'Blue'),
        ('B', 'Black'),
        ('R', 'Red'),
        ('G', 'Green'),
    )

	card_name = forms.CharField(required = False, max_length = 30, widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	rule_text = forms.CharField(required = False, max_length = 400)
	rarity = forms.ChoiceField(required = False, choices = RARITY_CHOICES)
	color = forms.ChoiceField(required = False, choices = COLOR_CHOICES)

class MTGSingleForm(forms.Form):
	CONDITION_CHOICES = (
        ('NM', 'Near Mint'),
        ('LP', 'Lightly Played'),
        ('MP', 'Moderately Played'),
        ('HP', 'Heavily Played'),
        ('DM', 'Damaged'),
    )

	LANGUAGE_CHOICE = (
        ('EN', 'English'),
        ('SP', 'Spanish'),
        ('FR', 'French'),
        ('DE', 'German'),
        ('IT', 'Italian'),
        ('PT', 'Portuguese'),
        ('JP', 'Japanese'),
        ('KR', 'Korean'),
        ('RU', 'Russian'),
        ('CS', 'Simplified Chinese'),
        ('CT', 'Traditional Chinese'),
    )


	# SKU_ID = forms.CharField(max_length=6, widget = forms.HiddenInput())
	condition = forms.ChoiceField(choices = CONDITION_CHOICES)
	language = forms.ChoiceField(choices = LANGUAGE_CHOICE)
	qty = forms.IntegerField()
	price = forms.DecimalField(max_digits=5, decimal_places=2,)
