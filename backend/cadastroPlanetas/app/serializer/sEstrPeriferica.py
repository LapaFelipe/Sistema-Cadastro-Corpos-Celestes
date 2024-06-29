from rest_framework import serializers

from app.models.EstrelaModel import Estrela
from app.models.EstrelaPerifericaModel import EstrPeriferica
from app.models.SistemaModel import Sistema


class EstrPerifericaSerializer(serializers.ModelSerializer):
    estrPeriferica_id_estrela = serializers.SlugRelatedField(
        queryset=Estrela.objects.all(),
        slug_field='id'
    )
    estrPeriferica_id_sistema = serializers.SlugRelatedField(
        queryset=Sistema.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = EstrPeriferica
        fields = '__all__'
