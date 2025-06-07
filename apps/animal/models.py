from django.db import models
from apps.tipo.models import Tipo
# Create your models here.
class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name='Nome do Animal')
    idade = models.PositiveIntegerField(verbose_name='Idade do Animal')
    tipo = models.ForeignKey(
        Tipo, 
        on_delete=models.CASCADE,
        related_name='animais',
        verbose_name='Tipo de Animal'
    )
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('adotado', 'Adotado'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='disponivel',
    )
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição do Animal')

    def __str__(self):
        return f"{self.nome} ({self.tipo.nome})"