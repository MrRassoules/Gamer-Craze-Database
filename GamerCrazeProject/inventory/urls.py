from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('mtgcards/', views.MTGCardListView.as_view(), name='mtgcards'),
    path('single/<str:pk>', views.MTGCardDetailView.as_view(), name='mtgcard-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
