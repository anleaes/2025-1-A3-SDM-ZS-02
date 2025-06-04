from .models import Adotante
from rest_framework import serializers

# Serializer para o modelo Adotante
class AdotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adotante
        fields = '__all__'