from django.db import models
from django.shortcuts import redirect

class PlanetaTipo(models.Model):
    id_planetTipo = models.AutoField(primary_key=True)
    desc_tipo = models.CharField(max_length=100)

