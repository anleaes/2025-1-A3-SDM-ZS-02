from django.shortcuts import render
from apps.adocaoitem.models import AdocaoItem
from .serializers import AdocaoItemSerializer
from rest_framework import viewsets

# Create your views here.
class AdocaoItemViewSet(viewsets.ModelViewSet):
    queryset = AdocaoItem.objects.all()
    serializer_class = AdocaoItemSerializer