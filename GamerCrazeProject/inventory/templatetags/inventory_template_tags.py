from django import template
from inventory.models import MTGCard, MTGSingle, MTGSet

register = template.Library()

@register.filter(name='mtg_singles')
def mtg_singles(MTGCard):
    mtg_singles = MTGSingle.objects.filter(SKU_ID = MTGCard.SKU_ID)
    singles = []
    for mtg_single in mtg_singles:
        singles.append(mtg_single)
    return singles
