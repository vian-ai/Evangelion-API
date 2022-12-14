from rest_framework import serializers
from ..models.models import Characters, EvaUnits, Evangelion

class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = ['id', 'name_en', 'name_jp', 'age', 'birthdate', 'zodiac', 'affiliations', 'title', 'height', 'weight', 'image']
        
class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaUnits
        fields = ['id', 'name_en', 'name_jp', 'model_type', 'pilot', 'soul', 'image']

class EvangelionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evangelion
        fields = ['id', 'title_en', 'title_jp', 'type', 'episodes', 'genre', 'released', 'logo', 'characters', 'units']
        depth = 2