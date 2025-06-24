from django.db import models

# Create your models here.

class Abrigo(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cnpj = models.CharField(max_length=14, unique=True, blank=True, null=True, default=None)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Abrigo"
        verbose_name_plural = "Abrigos"