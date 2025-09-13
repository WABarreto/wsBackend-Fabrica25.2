from rest_framework import serializers
from ..models import Pokemon, Moves

class PokemonSerializer (serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["name", "pokedex_id", "type1", "type2", "height", "weight", "location", "evolution_chain", "abilities"]
        read_only_fields = ["pokedex_id", "type1", "type2", "height", "weight", "location", "evolution_chain", "abilities"]

class MovesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Moves
        fields = ["name", "type", "category", "power", "accuracy", "pp"]
        read_only_fields = ["type", "category", "power", "accuracy", "pp"]