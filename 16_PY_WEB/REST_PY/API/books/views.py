from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Libro
from .serializers import LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
  serializer_class = LibroSerializer
  queryset = Libro.objects.all()