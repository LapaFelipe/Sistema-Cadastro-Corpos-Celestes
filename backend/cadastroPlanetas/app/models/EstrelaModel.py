from django.db import models

from app.models.CatTempCorModel import CatTempCor
from app.models.ConstelacaoModel import Constelacao
from app.models.CorpoModel import Corpo


class Estrela(models.Model):
    id_estrela = models.AutoField(primary_key=True)
    estr_nome = models.CharField(max_length=45, null=True, blank=True)
    estrela_tb_corpo = models.ForeignKey(Corpo, on_delete=models.CASCADE)
    estrela_id_constelacao = models.ForeignKey(Constelacao, on_delete=models.CASCADE)
    estrela_id_catCor = models.ForeignKey(CatTempCor, on_delete=models.CASCADE)