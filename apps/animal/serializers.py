from .models import Animal
from rest_framework import serializers

# serializer para o modelo animal
class Meta:
    model = Animal
    fields = '__all__'  # Inclui todos os campos do modelo