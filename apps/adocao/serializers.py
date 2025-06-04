from rest_framework import serializers
from apps.adotante.serializers import AdotanteSerializer
from apps.abrigo.serializers import AbrigoSerializer
from .models import AdocaoAbrigo

class AdocaoSerializer(serializers.ModelSerializer):
    adotante = AdotanteSerializer(source='adotante', read_only=True)
    abrigo = AbrigoSerializer(source='abrigo', read_only=True)

    class Meta:
        model = AdocaoAbrigo
        fields = [
            'id',
            'adotante',
            'abrigo',
            'status',
            'data_solicitacao',
            'data_atualizacao'
        ]
        read_only_fields = ['data_solicitacao', 'data_atualizacao']
