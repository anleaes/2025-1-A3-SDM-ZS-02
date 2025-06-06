from .models import checklist
from rest_framework import serializers

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = checklist
        fields = '__all__'