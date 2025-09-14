from rest_framework import serializers
from ..models import Pokemon, Moves

class MovesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Moves
        fields = ["name", "type", "category", "power", "accuracy", "pp"]
        read_only_fields = ["type", "category", "power", "accuracy", "pp"]

class PokemonSerializer (serializers.ModelSerializer):
    moves = MovesSerializer(many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = ["name", "pokedex_id", "type1", "type2", "height", "weight", "location", "evolution_chain", "abilities", "moves"]
        read_only_fields = ["pokedex_id", "type1", "type2", "height", "weight", "location", "evolution_chain", "abilities", "moves"]