from rest_framework import serializers

from app.models.EstrelaModel import Estrela
from app.models.GalaxiaModel import Galaxia
from app.models.SistemaModel import Sistema


class SistemaSerializer(serializers.ModelSerializer):
    sist_estrPrincipal = serializers.SlugRelatedField(
        queryset=Estrela.objects.all(),
        slug_field='id'
    )
    sist_galax = serializers.SlugRelatedField(
        queryset=Galaxia.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Sistema
        fields = '__all__'
