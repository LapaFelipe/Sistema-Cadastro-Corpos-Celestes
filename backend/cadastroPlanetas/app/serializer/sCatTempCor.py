from rest_framework import serializers

from app.models.CatTempCorModel import CatTempCor
from app.models.CategoriaModel import Categoria


class CatTempCorSerializer(serializers.ModelSerializer):
    CCT_corCat = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(),
        slug_field='cod_categoria'
    )

    class Meta:
        model = CatTempCor
        fields = '__all__'
