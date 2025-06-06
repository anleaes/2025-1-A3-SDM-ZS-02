from rest_framework import serializers
from apps.adotante.serializers import AdotanteSerializer
from apps.abrigo.serializers import AbrigoSerializer
from .models import AdocaoAbrigo
from apps.adotante.models import Adotante
from apps.abrigo.models import Abrigo

class AdocaoSerializer(serializers.ModelSerializer):
    adotante = serializers.PrimaryKeyRelatedField(queryset=Adotante.objects.all())
    abrigo = serializers.PrimaryKeyRelatedField(queryset=Abrigo.objects.all())
    adotante_nome = serializers.CharField(source='adotante.nome', read_only=True)
    abrigo_nome = serializers.CharField(source='abrigo.nome', read_only=True)
    class Meta:
        model = AdocaoAbrigo
        fields = [
            'id',
            'adotante',
            'abrigo',
            'status',
            'data_solicitacao',
            'data_atualizacao',
            'adotante_nome',
            'abrigo_nome'
        ]