from django.db import models
from django.shortcuts import redirect

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    nome_componente = models.CharField(max_length=100)