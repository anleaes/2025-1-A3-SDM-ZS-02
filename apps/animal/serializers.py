from .models import Animal
from rest_framework import serializers

# serializer para o modelo animal
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__' 