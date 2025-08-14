from django.urls import path
from . import views

urlpatterns = [
    # Altere aqui para usar a sua view `home`
    path('', views.home, name='home'),
]