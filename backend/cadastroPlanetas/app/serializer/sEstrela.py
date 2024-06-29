from rest_framework import serializers

from app.models.CatTempCorModel import CatTempCor
from app.models.ConstelacaoModel import Constelacao
from app.models.CorpoModel import Corpo
from app.models.EstrelaModel import Estrela


class EstrelaSerializer(serializers.ModelSerializer):
    estrela_tb_corpo = serializers.SlugRelatedField(
        queryset=Corpo.objects.all(),
        slug_field='id'
    )
    estrela_id_constelacao = serializers.SlugRelatedField(
        queryset=Constelacao.objects.all(),
        slug_field='id'
    )
    estrela_id_catCor = serializers.SlugRelatedField(
        queryset=CatTempCor.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Estrela
        fields = '__all__'