from django.forms import ModelForm
from inventory.models import *

class SearchForm(forms.Form):
	quantity = forms.IntegerField();
	price = forms.DecimalField();
class OrderItemForm(ModelForm):
	class Meta:
		model = OrderItem
		fields = '__all__'