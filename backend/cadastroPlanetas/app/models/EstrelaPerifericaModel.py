from django.db import models

from app.models.EstrelaModel import Estrela
from app.models.SistemaModel import Sistema


class EstrPeriferica(models.Model):
    id_estrPeriferica = models.AutoField(primary_key=True)
    estrPeriferica_id_estrela = models.ForeignKey(Estrela, on_delete=models.CASCADE)
    estrPeriferica_id_sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)