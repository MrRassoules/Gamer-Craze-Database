from django.shortcuts import render
from django.views import generic
from inventory.models import MTGSingle, MTGCard
from inventory.forms import ManageCardsForm

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cards = MTGSingle.objects.all().count()


    context = {
        'num_cards': num_cards,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def mtgcards_list(request):
    """View function for the list of cards"""
    
    # Check if theres a post request
    if request.method == 'POST':
        
        # Create the form
        form = ManageCardsForm(request.POST)
        

class MTGCardListView(generic.ListView):
    model = MTGCard
    

class MTGCardDetailView(generic.DetailView):
    model = MTGCard

