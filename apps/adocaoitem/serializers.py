from .models import AdocaoItem
from rest_framework import serializers
from apps.animal.models import Animal
from apps.adocao.models import AdocaoAbrigo

class AnimalSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'nome']



class AdocaoItemSerializer(serializers.ModelSerializer):
    animal = AnimalSimplesSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(
        source='animal',
        queryset=Animal.objects.all(),
        write_only=True
    )
    adocao_id = serializers.PrimaryKeyRelatedField(
        source='adocao',
        queryset=AdocaoAbrigo.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = AdocaoItem
        fields = ['id','adocao_id','animal','animal_id']
        