from .models import Tipo
from rest_framework import serializers

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'nome', 'descricao']