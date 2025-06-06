from .models import Checklist
from rest_framework import serializers

class ChecklistSerializer(serializers.ModelSerializer):
    animal_nome = serializers.CharField(source='animal.nome', read_only=True)
    vacina_nome = serializers.CharField(source='vacina.nome', read_only=True)
    
    class Meta:
        model = Checklist
        fields = ['id','animal_nome', 'vacina_nome','vacina', 'data_checklist']