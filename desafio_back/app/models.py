from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    evolution_chain = models.CharField(max_length=100)

    def __str__(self):
        return f"Nome: {self.name}, ID: {self.id}, Tipo 1: {self.type1}, Tipo 2: {self.type2}, Altura: {self.height}, Peso: {self.weight}, Localização: {self.location}, Linha evolutiva: {self.evolution_chain}"
