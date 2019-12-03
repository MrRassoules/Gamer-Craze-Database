from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from inventory.models import MTGSingle, MTGCard
from inventory.forms import *

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



class MTGCardDetailView(generic.DetailView):
    model = MTGCard

class MTGInventoryUpdate(UpdateView):
    model = MTGSingle
    fields = ['qty', 'price']
    template_name = 'manage.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('mtgcards')
