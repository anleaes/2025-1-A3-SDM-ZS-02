from .models import vacina
from rest_framework import serializers

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = vacina
        fields = '__all__'