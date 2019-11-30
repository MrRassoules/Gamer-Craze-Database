from django.contrib import admin
from .models import MTGSet, MTGCard, MTGSingle

@admin.register(MTGSet)
class MTGSetAdmin(admin.ModelAdmin):
    list_display = ('set_name', 'expansion_code')

@admin.register(MTGCard)
class MTGCardAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'set', 'number')

@admin.register(MTGSingle)
class MTGSingleAdmin(admin.ModelAdmin):

    list_display = ('card_name', 'set', 'condition', 'language', 'price')
