from .models import Abrigo
from rest_framework import viewsets
from .serializers import AbrigoSerializer
from django.shortcuts import render

# Create your views here.
class AbrigoViewSet(viewsets.ModelViewSet):
    queryset = Abrigo.objects.all()
    serializer_class = AbrigoSerializer