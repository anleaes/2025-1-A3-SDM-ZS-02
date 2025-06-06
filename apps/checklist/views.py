from django.shortcuts import render
from models import Checklist
from rest_framework import viewsets
from .serializers import ChecklistSerializer

# Create your views here.
class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer