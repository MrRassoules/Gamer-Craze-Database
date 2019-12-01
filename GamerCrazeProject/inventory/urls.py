from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mtgcards/', views.MTGCardListView.as_view(), name='mtgcards'),
]
