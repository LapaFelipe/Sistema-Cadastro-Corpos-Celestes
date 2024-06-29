from django.db import models
from django.shortcuts import redirect

class CiePesq(models.Model):
    id_CiePesq = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, default='None')
    instituicao = models.CharField(max_length=100, default='None')
    email = models.CharField(max_length=100,  default='None')
    senha = models.CharField(max_length=100, default='None')


