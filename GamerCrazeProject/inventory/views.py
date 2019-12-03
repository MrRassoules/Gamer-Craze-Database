from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from inventory.models import MTGSingle, MTGCard
from inventory.forms import SearchForm

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

class AdvancedSearch(FormView):
    model = MTGCard
    fields = ['card_name', 'rule_text', 'CARD_TYPE_CHOICES', 'COLOR_CHOICES', 'RARITY_CHOICES']
    template_name = 'advanced_search.html'
    form_class = SearchForm
    success_url = "/mtgcards/"
    
    def form_valid(self, form):
        context = {
            'test': "test",
        }
        return super().form_valid(form)
        

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
