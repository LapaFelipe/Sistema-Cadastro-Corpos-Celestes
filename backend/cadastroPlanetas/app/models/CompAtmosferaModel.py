from django.db import models

from app.models.ComponenteModel import Componente
from app.models.CorpoModel import Corpo


class CompAtmosfera(models.Model):
    cnt_componente = models.FloatField()
    compo_id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    compo_cod_corpo = models.ForeignKey(Corpo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('compo_id_componente', 'compo_cod_corpo')