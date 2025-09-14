from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["name", "pokedex_id", "type1", "type2", "height", "weight", "location", "abilities", "evolution_chain"]