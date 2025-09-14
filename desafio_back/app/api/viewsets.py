from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, DetailView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from ..models import Pokemon, Moves
from ..forms import PokemonForm
from .serializers import PokemonSerializer
from rest_framework.viewsets import ModelViewSet
import requests

class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name").strip()
        if not name:
            return render(request, self.template_name, {"error": "Digite o nome do Pokémon."})

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        if response.status_code != 200:
            return render(request, self.template_name, {"error": "Pokémon não encontrado. Verifique o nome e tente novamente."})

        data = response.json()
        type1 = data["types"][0]["type"]["name"] if len(data["types"]) > 0 else ""
        type2 = data["types"][1]["type"]["name"] if len(data["types"]) > 1 else "None"
        height = f"{round(data['height'] / 10, 2)} m"
        weight = f"{round(data['weight'] / 10, 2)} kg"
        location = ""
        abilities = ""
        evolution_chain_str = ""

        location_response = requests.get(data["location_area_encounters"])
        if location_response.status_code == 200:
            locations = location_response.json()
            location = ", ".join(set([loc["location_area"]["name"] for loc in locations])) if locations else ""

        for ability in data.get("abilities", []):
            ability_name = ability["ability"]["name"]
            if ability["is_hidden"]:
                ability_name += " (Hidden)"
            abilities += ability_name + ", "
        abilities = abilities.rstrip(", ")


        species_response = requests.get(data["species"]["url"])
        if species_response.status_code == 200:
            species_data = species_response.json()
            evo_response = requests.get(species_data["evolution_chain"]["url"])
            if evo_response.status_code == 200:
                chain = evo_response.json()["chain"]
                evolution_chain = []
                while chain:
                    evolution_chain.append(chain["species"]["name"])
                    chain = chain["evolves_to"][0] if chain["evolves_to"] else None
                evolution_chain_str = " -> ".join(evolution_chain)

        pokemon_instance, created = Pokemon.objects.get_or_create(
            name=name.lower(),
            defaults={
                "pokedex_id": data.get("id", ""),
                "type1": type1,
                "type2": type2,
                "height": height,
                "weight": weight,
                "location": location,
                "abilities": abilities,
                "evolution_chain": evolution_chain_str
            }
        )

        if created: 
            for move in data.get("moves", []):
                move_name = move["move"]["name"]
                move_response = requests.get(f"https://pokeapi.co/api/v2/move/{move_name}")
                if move_response.status_code == 200:
                    move_data = move_response.json()
                    Moves.objects.create(
                        name=move_data["name"],
                        type=move_data["type"]["name"],
                        category=move_data["damage_class"]["name"],
                        power=move_data["power"] if move_data["power"] else "None",
                        accuracy=move_data["accuracy"] if move_data["accuracy"] else "None",
                        pp=move_data["pp"] if move_data["pp"] else "None",
                        pokemon=pokemon_instance
                    )

        return redirect("pokemon_lista")

class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = "pokemon_detail.html"
    context_object_name = "pokemon"

class PokemonListView(ListView):
    model = Pokemon
    template_name = "pokemon_lista.html"
    context_object_name = "pokemons"


class PokemonDeleteView(DeleteView):
    model = Pokemon
    success_url = reverse_lazy("pokemon_lista")

class PokemonUpdateView(UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "pokemon_update.html"
    success_url = reverse_lazy("pokemon_lista") 

class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

