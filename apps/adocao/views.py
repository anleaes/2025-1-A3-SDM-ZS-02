from django.shortcuts import render
from rest_framework import viewsets
from .models import AdocaoAbrigo
from .serializers import AdocaoSerializer

# Create your views here.
class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = AdocaoAbrigo.objects.all()
    serializer_class = AdocaoSerializer
