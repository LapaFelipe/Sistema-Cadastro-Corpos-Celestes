from django.db import models

from app.models.EstrelaModel import Estrela
from app.models.GalaxiaModel import Galaxia


class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True)
    desc_sistema = models.CharField(max_length=100, null=True, blank=True)
    sist_estrPrincipal = models.ForeignKey(Estrela, on_delete=models.CASCADE)
    sist_galax = models.ForeignKey(Galaxia, on_delete=models.CASCADE)
