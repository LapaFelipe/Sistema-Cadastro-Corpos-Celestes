from rest_framework import serializers

from app.models.CompAtmosferaModel import CompAtmosfera
from app.models.ComponenteModel import Componente
from app.models.CorpoModel import Corpo


class CompAtmosferaSerializer(serializers.ModelSerializer):
    compo_id_componente = serializers.SlugRelatedField(
        queryset=Componente.objects.all(),
        slug_field='id'
    )
    compo_cod_corpo = serializers.SlugRelatedField(
        queryset=Corpo.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = CompAtmosfera
        fields = '__all__'
