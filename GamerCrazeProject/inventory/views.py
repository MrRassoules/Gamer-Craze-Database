from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
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

def AdvancedSearch(request):
    model = MTGCard
    template_name = 'advanced_search.html'
    form = SearchForm(request.POST)
    card_name = ""
    rule_text = ""
    rarity = ""
    color = ""

    if request.method == "POST":
        if form.is_valid():
            card_name = form.cleaned_data["card_name"]
            rule_text = form.cleaned_data["rule_text"]
            rarity = form.cleaned_data["rarity"]
            color = form.cleaned_data["color"]
        else:
            form = SearchForm()
    context = {
        "form": form,
        "card_name": card_name,
        'rule_text': rule_text,

        'model': model.objects.all().filter(
            card_name__contains = card_name,
            rule_text__contains = rule_text,
            rarity__contains = rarity,
            color__contains = color,
        ),
        'rarity': rarity,
        'color': color,
    }

    return render(request, 'advanced_search.html', context)


def MTGInventoryAdd(request, **kwargs):
    model = MTGSingle
    template_name = 'add_single.html'
    form = MTGSingleForm(request.POST)
    mtgcard = MTGCard.objects.get(pk=kwargs['pk'],)

    if request.method == "POST":
        if form.is_valid():
            new_single = MTGSingle(
                SKU_ID = MTGCard.objects.get(SKU_ID=kwargs['pk']),
                condition = form.cleaned_data['condition'],
                language = form.cleaned_data['language'],
                qty = form.cleaned_data['qty'],
                price = form.cleaned_data['price'],
            )
            new_single.save()
            return redirect('mtgcards')
        else:
            form = MTGSingleForm()
    return render(request, 'add_single.html', {'form': form})


class MTGCardDetailView(generic.DetailView):
    model = MTGCard


    def make_order_item(request, self):

        # if this is a POST request we need to process the form data
        if request.method == 'POST':

            single = Single.objects.get(pk=self.pk)

            # create a form instance and populate it with data from the request
            form = OrderItemForm(initial={'order_id': 1, 'single_id': single.pk, 'qty': request.POST, 'total_price': (single.price * request.POST)})
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                form.save()

        # if a GET (or any other method) we'll create a blank form
        else:
            form = OrderItemForm()

        return render(request, 'MTGCard_detail.html', {'form': form})

class MTGInventoryUpdate(UpdateView):
    model = MTGSingle
    fields = ['qty', 'price']
    template_name = 'manage.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('mtgcards')
