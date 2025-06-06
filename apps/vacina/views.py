from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import VacinaSerializer

# Create your views here.
class VacinaViewSet(viewsets.ModelViewSet):
    queryset = VacinaSerializer.Meta.model.objects.all()
    serializer_class = VacinaSerializer