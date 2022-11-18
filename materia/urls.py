from django.urls import path
from .views.materia_views import MateriasView, MateriaDetailView
from .views.spell_views import SpellsView, SpellDetailView

urlpatterns = [
    path('', MateriasView.as_view(), name='materias'),
    path('<int:pk>/', MateriaDetailView.as_view(), name='materia'),
    path('spells/', SpellsView.as_view(), name='spells'),
    path('spells/<int:pk>',SpellDetailView.as_view(), name='spell')
]