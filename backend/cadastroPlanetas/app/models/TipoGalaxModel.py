from django.db import models


class TipoGalax(models.Model):
    id_tipoGalax = models.AutoField(primary_key=True)
    desc_tipoGalax = models.CharField(max_length=45)
