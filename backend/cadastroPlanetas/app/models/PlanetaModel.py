from django.db import models

from app.models.CorpoModel import Corpo
from app.models.PlanetaTipoModel import PlanetaTipo
from app.models.SistemaModel import Sistema


class Planeta(models.Model):
    id_planeta = models.AutoField(primary_key=True)
    desc_planeta = models.CharField(max_length=100)
    vel_orb_kms = models.DecimalField(max_digits=10, decimal_places=2)
    diam_equatorial = models.DecimalField(max_digits=10, decimal_places=2)
    period_rotacao = models.FloatField()
    gravidade = models.DecimalField(max_digits=10, decimal_places=2)
    plan_codCorpo = models.ForeignKey(Corpo, on_delete=models.CASCADE)
    plan_planetaTipo = models.ForeignKey(PlanetaTipo, on_delete=models.CASCADE)
    plan_id_sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)