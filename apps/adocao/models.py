from django.db import models
from adotantes.models import Adotante
from abrigos.models import Abrigo

# Create your models here.
class AdotanteAbrigo(models.Model):
    status_choices = [
        ('aceito', 'Aceito'),
        ('rejeitado', 'Rejeitado'),
        ('pendente', 'Pendente'),
        
    ]
    adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE, related_name='adotante_abrigos')
    abrigo = models.ForeignKey(Abrigo, on_delete=models.CASCADE, related_name='abrigo_adotantes')
    status = models.CharField(max_length=10, choices=status_choices, default='pendente')
    class Meta:
        verbose_name = 'Abrigo do Adotante'
        verbose_name_plural = 'Abrigos dos Adotantes'
        ordering = ['id']
        unique_together = ('adotante', 'abrigo')

    def __str__(self):
        return f"{self.adotante.nome} - {self.abrigo.nome}"
