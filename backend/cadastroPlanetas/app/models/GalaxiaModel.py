from django.db import models

from app.models.TipoGalaxModel import TipoGalax


class Galaxia(models.Model):
    id_galaxia = models.AutoField(primary_key=True)
    galax_desc = models.CharField(max_length=45)
    galax_tipoGalax = models.ForeignKey(TipoGalax, on_delete=models.CASCADE)