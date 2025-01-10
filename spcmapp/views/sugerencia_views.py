from ..serializers import SugerenciaSerializer, ActividadSerializer
from ..models import Sugerencias, Actividad
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.generics import ListAPIView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

class IsAdminUser(BasePermission):
    """
    Permitir acceso solo a usuarios con rol de administrador.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class SugerenciaAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        """
        Obtener todas las sugerencias del usuario autenticado.
        Si el usuario es admin, obtiene todas las sugerencias del sistema.
        """
        if request.user.is_staff:  
            sugerencias = Sugerencias.objects.all()
        else:  
            sugerencias = Sugerencias.objects.filter(user=request.user)

        serializer = SugerenciaSerializer(sugerencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        """Crear una nueva sugerencia"""
        serializer = SugerenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SugerenciaDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk, user):
        """Obtener una sugerencia específica por su ID"""
        return get_object_or_404(Sugerencias, pk=pk, user=user)

    def put(self, request, pk):
        """Actualizar una sugerencia existente"""
        sugerencia = self.get_object(pk, request.user)
        serializer = SugerenciaSerializer(sugerencia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Eliminar una sugerencia"""
        sugerencia = self.get_object(pk, request.user)
        sugerencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ActividadListView(APIView):
    def get(self, request):
        actividades = Actividad.objects.all()  
        serializer = ActividadSerializer(actividades, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)