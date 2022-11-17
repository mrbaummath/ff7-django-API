from rest_framework import serializers

from .models import Materia

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Materia