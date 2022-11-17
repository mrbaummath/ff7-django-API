from django.urls import path
from .views import MateriasView, MateriaDetailView

urlpatterns = [
    path('', MateriasView.as_view(), name='materias'),
    path('<int:pk>/', MateriaDetailView.as_view(), name='materia')
]