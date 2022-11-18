from ..serializers import MateriaSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.materia import Materia


# Create your views here.
class MateriasView(APIView):
    """View class for materia/ for viewing all and creating"""
    serializer_class = MateriaSerializer
    def get(self, request):
        materias = Materia.objects.all()
        serializer = MateriaSerializer(materias, many=True)
        return Response({'materias':serializer.data})
    def post(self, request):
        serializer = MateriaSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MateriaDetailView(APIView):
    """View class for materia/:pk for viewing a single materia, updating a single materia, or rmoving a single materia"""
    def get(self, request,pk):
        materia = get_object_or_404(Materia, pk=pk)
        serializer = MateriaSerializer(materia)
        return Response({'materia':serializer.data})
    def patch(self, request, pk):
        materia = get_object_or_404(Materia, pk=pk)
        serializer = MateriaSerializer(materia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        materia = get_object_or_404(Materia, pk=pk)
        materia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)