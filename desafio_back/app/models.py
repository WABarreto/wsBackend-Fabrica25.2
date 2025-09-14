from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length = 500)
    pokedex_id = models.CharField(max_length = 500)
    type1 = models.CharField(max_length = 500)
    type2 = models.CharField(max_length = 500)
    height = models.CharField(max_length = 500)
    weight = models.CharField(max_length = 500)
    location = models.CharField(max_length = 500)
    evolution_chain = models.CharField(max_length = 500)
    abilities = models.CharField(max_length = 500)

    def __str__(self):
        return f"Nome: {self.name}, ID: {self.pokedex_id}, Tipo 1: {self.type1}, Tipo 2: {self.type2}, Altura: {self.height}, Peso: {self.weight}, Localização: {self.location}, Linha evolutiva: {self.evolution_chain}, Habilidades: {self.abilities}"
    
class Moves(models.Model):
    name = models.CharField(max_length = 500)
    type = models.CharField(max_length = 500)
    category = models.CharField(max_length = 500)
    power = models.CharField(max_length = 500)
    accuracy = models.CharField(max_length = 500)
    pp = models.CharField(max_length = 500)
    pokemon = models.ForeignKey(Pokemon, related_name="moves", on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"Nome: {self.name}, Tipo: {self.type}, Categoria: {self.category}, Poder: {self.power}, Precisão: {self.accuracy}, PP: {self.pp}"


