from rest_framework import serializers
from ..models import Info

class InfoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['name', 'id', 'type1', 'type2', 'height', 'weight', 'location', 'evolution_chain']
        read_only_fields = ['id','type1', 'type2', 'height', 'weight', 'location', 'evolution_chain']