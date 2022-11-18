from django.db import models

# Create your models here.

class Materia(models.Model):
    GREEN = 'G'
    YELLOW = 'Y'
    PURPLE = 'P'
    RED = 'R'
    BLUE = 'B'
    COLOR_CHOICES = [
        (GREEN, 'Green'),
        (YELLOW, 'Yellow'),
        (PURPLE, 'Purple'),
        (RED, 'Red'),
        (BLUE, 'Blue'),
    ]
    name= models.CharField(max_length=20, default ='')
    color= models.CharField(
        max_length = 1,
        choices = COLOR_CHOICES,
        default = 'G'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.color} Materia: {self.name}"
    
    
    
