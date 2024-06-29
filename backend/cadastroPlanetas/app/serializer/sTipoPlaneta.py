from rest_framework import serializers
from app.models.PlanetaTipoModel import PlanetaTipo


class TipoPlanetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetaTipo
        fields = '__all__'
