from django.shortcuts import render
from .models import Tipo
from rest_framework import viewsets
from .serializers import TipoSerializer
# Create your views here.

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer