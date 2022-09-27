from rest_framework import viewsets
from rest_framework.response import Response
from ..models.models import EvaUnits, Evangelion, Characters
from ..serializers.serializer import EvangelionSerializer, CharactersSerializer, UnitsSerializer

class EvangelionViewsSet(viewsets.ModelViewSet):
    serializer_class = EvangelionSerializer
    
    def get_queryset(self):
        eva = Evangelion.objects.all()
        return eva
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        new_eva = Evangelion.objects.create(
            title_en=data["title_en"],
            title_jp=data["title_jp"],
            type=data["type"],
            episodes=data["episodes"],
            genre=data["genre"],
            released=data["released"],
            logo=data["logo"]
        )
        
        new_eva.save()
        
        for character in data["characters"]:
            character_obj = Characters.objects.get(name_en=character["name_en"])
            new_eva.characters.add(character_obj)
            
        for evaUnit in data["units"]:
            evaUnit_obj = EvaUnits.objects.get(name_en=evaUnit["name_en"])
            new_eva.units.add(evaUnit_obj)
            
        serializer = EvangelionSerializer(new_eva)
        
        return Response(serializer.data)

class CharactersViewSet(viewsets.ModelViewSet):
    serializer_class = CharactersSerializer

    def get_queryset(self):
        character = Characters.objects.all()
        return character
    
class UnitsViewSet(viewsets.ModelViewSet):
    serializer_class = UnitsSerializer
    
    def get_queryset(self):
        unit = EvaUnits.objects.all()
        return unit