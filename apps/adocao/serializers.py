from rest_framework import serializers
from apps.adotante.serializers import AdotanteSerializer
from apps.abrigo.serializers import AbrigoSerializer
from .models import AdocaoAbrigo

class AdocaoSerializer(serializers.ModelSerializer):
    adotante = AdotanteSerializer(read_only=True)
    abrigo = AbrigoSerializer(read_only=True)

    class Meta:
        model = AdocaoAbrigo
        fields = '__all__'