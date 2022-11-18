from rest_framework import serializers

from .models import Spell

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Spell

class SpellReadSerializer(serializers.ModelSerializer):
    materia = serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Spell
        