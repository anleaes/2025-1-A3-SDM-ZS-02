from django.shortcuts import render
from rest_framework import viewsets
from .models import AdocaoAbrigo
from .serializers import AdocaoSerializer

# Create your views here.
class AdocaoViewSet(viewsets.ModelViewSet):
    queryset = AdocaoAbrigo.objects.all()
    serializer_class = AdocaoSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status == 'aceito':
            for item in instance.itens.all(): 
                item.animal.status = 'adotado'
                item.animal.save()