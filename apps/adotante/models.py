from django.db import models

# Create your models here.
class Adotante(models.Model):
    #estrutura do modelo Adotante a principio
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

  