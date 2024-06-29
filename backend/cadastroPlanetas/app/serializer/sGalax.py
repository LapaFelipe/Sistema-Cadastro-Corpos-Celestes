from rest_framework import serializers

from app.models.GalaxiaModel import Galaxia
from app.models.TipoGalaxModel import TipoGalax


class GalaxiaSerializer(serializers.ModelSerializer):
    galax_tipoGalax = serializers.SlugRelatedField(
        queryset=TipoGalax.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Galaxia
        fields = '__all__'