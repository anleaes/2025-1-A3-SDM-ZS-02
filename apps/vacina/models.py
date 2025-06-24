from django.db import models
# Create your models here.

class Vacina(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome da Vacina')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição da Vacina')

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'

    def __str__(self):
        return f"{self.nome} - {self.descricao[:50]}"