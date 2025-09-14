"""
URL configuration for desafio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api.viewsets import PokemonViewSet, PokemonDetailView, HomeView, PokemonListView, PokemonDeleteView, PokemonUpdateView

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("pokemon/<int:pk>/", PokemonDetailView.as_view(), name="pokemon_detail"), 
    path('pokemon/', PokemonListView.as_view(), name='pokemon_lista'),
    path('home/', HomeView.as_view(), name='home'), 
    path("pokemon/<int:pk>/delete/", PokemonDeleteView.as_view(), name="pokemon_delete"),
    path("pokemon/<int:pk>/update/", PokemonUpdateView.as_view(), name="pokemon_update"),
]
