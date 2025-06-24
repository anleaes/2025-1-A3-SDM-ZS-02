from django.shortcuts import render
from .models import Adotante
from rest_framework import viewsets
from .serializers import AdotanteSerializer

# Create your views here.

#class AdotanteViewSet
# ViewSet para o modelo Adotante
class AdotanteViewSet(viewsets.ModelViewSet):
    queryset = Adotante.objects.all()
    serializer_class = AdotanteSerializer