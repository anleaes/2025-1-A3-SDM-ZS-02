from django.db import models

# Create your models here.
class Tipo(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome do Tipo')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição do Tipo')

    class Meta:
        verbose_name = 'Tipo de Animal'
        verbose_name_plural = 'Tipos de Animais'
        ordering = ['nome']

    def __str__(self):
        return self.nome