from django.db import models
from apps.vacina.models import Vacina
from apps.animal.models import Animal
# Create your models here.

class Checklist(models.Model):
    animal = models.ForeignKey(
        Animal, 
        on_delete=models.CASCADE, 
        related_name='checklists'
    )
    vacina = models.ForeignKey(
        Vacina, 
        on_delete=models.CASCADE, 
        related_name='checklists'
    )
    data_checklist = models.DateField(
        auto_now_add=True, 
        verbose_name='Data do Checklist'
    )

    class Meta:
        verbose_name = 'Checklist de Adoção'
        verbose_name_plural = 'Checklists de Adoção'
        unique_together = ('animal', 'vacina')

    def __str__(self):
        return f"Checklist para {self.animal.nome} - Vacina: {self.vacina.nome} - Data: {self.data_checklist.strftime('%d/%m/%Y')}"