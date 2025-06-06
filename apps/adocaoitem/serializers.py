from .models import AdocaoItem
from rest_framework import serializers
class AdocaoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdocaoItem
        fields = '__all__'
        