from rest_framework import serializers
from ..models import Pokemon

class PokemonSerializer (serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'pokedex_id', 'type1', 'type2', 'height', 'weight', 'location', 'evolution_chain']
        read_only_fields = ['pokedex_id', 'type1', 'type2', 'height', 'weight', 'location', 'evolution_chain']