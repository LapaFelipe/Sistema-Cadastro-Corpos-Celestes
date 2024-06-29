from rest_framework import serializers

from app.models.CorpoModel import Corpo
from app.models.PlanetaModel import Planeta
from app.models.SatNaturalModel import SatNatural


class SatNaturalSerializer(serializers.ModelSerializer):
    satNat_corpo = serializers.SlugRelatedField(
        queryset=Corpo.objects.all(),
        slug_field='id'
    )
    satNat_planet = serializers.SlugRelatedField(
        queryset=Planeta.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = SatNatural
        fields = '__all__'