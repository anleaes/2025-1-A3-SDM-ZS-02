from .models import Abrigo
from rest_framework import serializers

class AbrigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrigo
        fields = '__all__'