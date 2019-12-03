from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('mtgcards/', views.MTGCardListView.as_view(), name='mtgcards'),
    path('single/<str:pk>', views.MTGCardDetailView.as_view(), name='mtgcard-detail'),
    path('manage/<int:pk>', views.MTGInventoryUpdate.as_view(), name='mtg_single-update')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
