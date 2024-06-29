from rest_framework import serializers

from app.models.ConstelacaoModel import Constelacao


class ConstelacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constelacao
        fields = '__all__'