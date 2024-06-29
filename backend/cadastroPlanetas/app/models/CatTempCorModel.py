from django.db import models

from app.models.CategoriaModel import Categoria


class CatTempCor(models.Model):
    id_CatCorTemp = models.AutoField(primary_key=True)
    tempK_ini = models.IntegerField()
    tempK_fim = models.IntegerField()
    CCT_corCat = models.ForeignKey(Categoria, on_delete=models.CASCADE)