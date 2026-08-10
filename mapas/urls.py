from django.urls import path
from . import views

urlpatterns = [
    # Aquí sí llamamos a las vistas
    path('', views.mapa_view, name='mapa_principal'),
    path('api/puntos/', views.get_puntos, name='api_puntos'),
]