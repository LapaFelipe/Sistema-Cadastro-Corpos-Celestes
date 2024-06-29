from django.db import models

class Categoria(models.Model):
    cod_categoria = models.AutoField(primary_key=True)
    categoria_nome = models.CharField(max_length=100)