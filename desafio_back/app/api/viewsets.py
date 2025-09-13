from rest_framework.viewsets import ModelViewSet
from ..models import Pokemon
from .serializers import PokemonSerializer
import requests

class PokemonViewSet(ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        if response.status_code == 200:
            data = response.json()
            type1 = data['types'][0]['type']['name'] if len(data['types']) > 0 else ''
            type2 = data['types'][1]['type']['name'] if len(data['types']) > 1 else 'None'
            height = f"{round(data['height'] / 10, 2)} m"
            weight = f"{round(data['weight'] / 10, 2)} kg"
            location_response = requests.get(data['location_area_encounters'])
            if location_response.status_code == 200:
                locations = location_response.json()
                location = ', '.join(set([loc['location_area']['name'] for loc in locations])) if locations else ''
            else:
                location = ''
            species_response = requests.get(data['species']['url'])
            if species_response.status_code == 200:
                species_data = species_response.json()
                evolution_chain_url = species_data['evolution_chain']['url']
                evolution_response = requests.get(evolution_chain_url)
                if evolution_response.status_code == 200:
                    evolution_data = evolution_response.json()
                    chain = evolution_data['chain']
                    evolution_chain = []
                    while chain:
                        evolution_chain.append(chain['species']['name'])
                        chain = chain['evolves_to'][0] if chain['evolves_to'] else None
                    evolution_chain_str = ' -> '.join(evolution_chain)
                else:
                    evolution_chain_str = ''
            else:
                evolution_chain_str = ''
            serializer.save(
                pokedex_id=data.get('id', None),
                type1=type1,
                type2=type2,
                height=height,
                weight=weight,
                location=location,
                evolution_chain=evolution_chain_str
            )
        else:
            serializer.save(
                pokedex_id='',
                type1='',
                type2='',
                height='',
                weight='',
                location='',
                evolution_chain=''
            )

