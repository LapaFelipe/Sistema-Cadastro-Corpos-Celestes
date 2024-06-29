from app.models.TipoGalaxModel import TipoGalax
from rest_framework import serializers


class TipoGalaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoGalax
        fields = '__all__'
