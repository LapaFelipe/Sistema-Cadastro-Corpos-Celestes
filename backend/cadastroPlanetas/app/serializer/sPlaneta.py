from rest_framework import serializers

from app.models.CorpoModel import Corpo
from app.models.PlanetaModel import Planeta
from app.models.PlanetaTipoModel import PlanetaTipo
from app.models.SistemaModel import Sistema


class PlanetaSerializer(serializers.ModelSerializer):
    plan_codCorpo = serializers.SlugRelatedField(
        queryset=Corpo.objects.all(),
        slug_field='id'
    )
    plan_planetaTipo = serializers.SlugRelatedField(
        queryset=PlanetaTipo.objects.all(),
        slug_field='id'
    )
    plan_id_sistema = serializers.SlugRelatedField(
        queryset=Sistema.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Planeta
        fields = '__all__'
