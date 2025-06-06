from django.db import models
from apps.animal.models import Animal
from apps.adocao.models import AdocaoAbrigo
# Create your models here.
class AdocaoItem(models.Model):
    # Modelo para gerenciar os itens de adoção
    adocao = models.ForeignKey(
        AdocaoAbrigo, 
        on_delete=models.CASCADE, 
        related_name='itens_adocao'
    )
    animal = models.ForeignKey(
        Animal, 
        on_delete=models.CASCADE, 
        related_name='itens_adocao'
    )

    class Meta:
        verbose_name = 'Item de Adoção'
        verbose_name_plural = 'Itens de Adoção'
        unique_together = ('adocao', 'animal')

    def __str__(self):
        return f"{self.animal.nome} - {self.quantidade} item(s) na adoção {self.adocao.id}"