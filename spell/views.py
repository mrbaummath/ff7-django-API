from .serializers import SpellSerializer, SpellReadSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Spell


# Create your views here.
class SpellsView(APIView):
    """View class for spells/ for viewing all and creating"""
    serializer_class = SpellSerializer
    def get(self, request):
        spells = Spell.objects.all()
        serializer = SpellReadSerializer(spells, many=True)
        return Response({'spells':serializer.data})
    def post(self, request):
        serializer = SpellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpellDetailView(APIView):
    """View class for spells/:pk for viewing a single spell, updating a single spell, or rmoving a single spell"""
    def get(self, request,pk):
        spell = get_object_or_404(Spell, pk=pk)
        serializer = SpellReadSerializer(spell)
        return Response({'spell':serializer.data})
    def patch(self, request, pk):
        spell = get_object_or_404(Spell, pk=pk)
        serializer = SpellSerializer(spell, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        spell = get_object_or_404(Spell, pk=pk)
        spell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)