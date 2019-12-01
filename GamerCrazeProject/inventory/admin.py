from django.contrib import admin
from .models import MTGSet, MTGCard, MTGSingle, Order, OrderItem

@admin.register(MTGSet)
class MTGSetAdmin(admin.ModelAdmin):
    list_display = ('expansion_code', 'set_name')

@admin.register(MTGCard)
class MTGCardAdmin(admin.ModelAdmin):
    list_display = ('SKU_ID','card_name', 'set', 'number')

@admin.register(MTGSingle)
class MTGSingleAdmin(admin.ModelAdmin):
    list_display = ('card_name', 'set', 'condition', 'language', 'qty', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_id')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product', 'qty')
