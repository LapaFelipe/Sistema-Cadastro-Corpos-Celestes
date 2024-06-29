from django.db import models

from app.models.CorpoModel import Corpo
from app.models.PlanetaModel import Planeta


class SatNatural(models.Model):
    cod_satNat = models.AutoField(primary_key=True)
    satNat_nome = models.CharField(max_length=100)
    satNat_corpo = models.ForeignKey(Corpo, on_delete=models.CASCADE)
    satNat_planet = models.ForeignKey(Planeta, on_delete=models.CASCADE)