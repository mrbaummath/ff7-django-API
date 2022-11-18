from rest_framework import serializers

from .models.materia import Materia
from .models.spell import Spell

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Materia


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Spell

class SpellReadSerializer(serializers.ModelSerializer):
    materia = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Spell
        