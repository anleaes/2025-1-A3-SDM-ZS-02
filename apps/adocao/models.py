from django.db import models
from apps.adotante.models import Adotante
from apps.abrigo.models import Abrigo

class AdocaoAbrigo(models.Model):
    #Modelo para gerenciar as adoções entre adotantes e abrigos

    #Escolha de status para a adoção
    status_choices = [
        ('aceito', 'Aceito'),
        ('rejeitado', 'Rejeitado'),
        ('pendente', 'Pendente'),
    ]
    # foreign key para o modelo Adotante e Abrigo
    # trazendo a class Adotante e Abrigo
    # e definindo o relacionamento com o modelo Adoção
    adotante = models.ForeignKey(
        Adotante, 
        on_delete=models.CASCADE, 
        related_name='adocoes'  
    )
    abrigo = models.ForeignKey(
        Abrigo, 
        on_delete=models.CASCADE, 
        related_name='adocoes'  
    )
    status = models.CharField(
        max_length=10, 
        choices=status_choices, 
        default='pendente'
    )
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Adoção'
        verbose_name_plural = 'Adoções'
        ordering = ['-data_solicitacao']
        unique_together = ('adotante', 'abrigo')

    def __str__(self):
        return f"Adoção: {self.adotante.nome} - {self.abrigo.nome} ({self.status})"
