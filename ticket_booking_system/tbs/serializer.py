from rest_framework import serializers
from .models import Ticket, Person, Movie

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = ['p_id', 'name', 'number']

class TicketSerializer(serializers.ModelSerializer):
    #person = serializers.RelatedField(source=, read_only=True)
    #movie = serializers.RelatedField(source='movie', read_only=True)
    class Meta:
        model= Ticket
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields = ['m_id', 'name']