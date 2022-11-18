from django.db import models
from ..materia.models import Materia

class Spell(models.Model):
    name= models.CharField(max_length=100)
    mp_cost = models.IntegerField()
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='spells'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cost': self.mp_cost,
        }