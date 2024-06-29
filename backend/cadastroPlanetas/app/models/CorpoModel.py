from django.db import models
from django.shortcuts import redirect
from app.models.CiePesqModel import CiePesq


class Corpo(models.Model):
    cod_corpo = models.AutoField(primary_key=True)
    dta_descoberta = models.IntegerField(null=True, blank=True)
    corpo_CiePesq = models.ForeignKey(CiePesq, on_delete=models.CASCADE)