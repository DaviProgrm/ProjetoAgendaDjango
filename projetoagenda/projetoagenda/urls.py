from django.contrib import admin
from django.urls import path
from authentication import views
from django.views.generic import RedirectView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda')),
]
