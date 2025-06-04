from django.db import models

# Create your models here.

class Abrigo(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    