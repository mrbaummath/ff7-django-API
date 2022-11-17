from django.urls import path
from .views import CharactersView, CharacterDetailView

urlpatterns = [
    path('', CharactersView.as_view(), name='characters'),
    path('<int:pk>/', CharacterDetailView.as_view(), name='character')
]