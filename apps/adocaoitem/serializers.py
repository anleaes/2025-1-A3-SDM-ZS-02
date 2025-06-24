from .models import AdocaoItem
from rest_framework import serializers
from apps.animal.models import Animal
from apps.adocao.models import AdocaoAbrigo

class AnimalSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'nome','imagem']

class AdocaoItemSimplesSerializer(serializers.ModelSerializer):
    animal = AnimalSimplesSerializer(read_only=True)

    class Meta:
        model = AdocaoItem
        fields = ['id', 'animal']

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        animal_adotados = AdocaoItem.objects.filter(adocao__status='aceito').values_list('animal_id', flat=True)
        self.fields['animal_id'].queryset = Animal.objects.exclude(id__in=animal_adotados)

    class Meta:
        model = AdocaoItem
        fields = ['id', 'adocao_id', 'animal', 'animal_id']
