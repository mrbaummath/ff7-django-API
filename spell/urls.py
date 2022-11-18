from django.urls import path
from .views import SpellsView, SpellDetailView

urlpatterns = [
    path('', SpellsView.as_view(), name='spells'),
    path('<int:pk>/', MateriaDetailView.as_view(), name='spell')
]