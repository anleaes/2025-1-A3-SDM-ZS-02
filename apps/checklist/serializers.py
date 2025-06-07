from .models import Checklist
from rest_framework import serializers
from apps.animal.models import Animal
from apps.vacina.models import Vacina

class ChecklistSerializer(serializers.ModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.filter(status='disponivel'))
    vacina = serializers.PrimaryKeyRelatedField(queryset=Vacina.objects.all())

    animal_nome = serializers.CharField(source='animal.nome', read_only=True)
    vacina_nome = serializers.CharField(source='vacina.nome', read_only=True)
    descricao_vacina = serializers.CharField(source='vacina.descricao', read_only=True)

    class Meta:
        model = Checklist
        fields = ['id','animal','vacina','animal_nome', 'vacina_nome', 'data_checklist', 'descricao_vacina']