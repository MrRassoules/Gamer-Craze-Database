from django.shortcuts import render
from django.views import generic
from inventory.models import MTGSingle, MTGCard

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cards = MTGSingle.objects.all().count()


    context = {
        'num_cards': num_cards,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MTGCardListView(generic.ListView):
    model = MTGCard

    
