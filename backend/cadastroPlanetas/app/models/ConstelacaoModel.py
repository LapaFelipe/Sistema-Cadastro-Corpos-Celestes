from django.db import models

class Constelacao(models.Model):
    id_constelacao = models.AutoField(primary_key=True)
    const_desc = models.CharField(max_length=100)