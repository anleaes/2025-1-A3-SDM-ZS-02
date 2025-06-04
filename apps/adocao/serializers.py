from rest_framework import serializers
from apps.adotante.serializers import AdotanteSerializer
from apps.abrigo.serializers import AbrigoSerializer
from .models import AdocaoAbrigo
from apps.adotante.models import Adotante
from apps.abrigo.models import Abrigo

class AdocaoSerializer(serializers.ModelSerializer):
    adotante = serializers.PrimaryKeyRelatedField(queryset=Adotante.objects.all())
    abrigo = serializers.PrimaryKeyRelatedField(queryset=Abrigo.objects.all())

    class Meta:
        model = AdocaoAbrigo
        fields = '__all__'