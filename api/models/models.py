from django.db import models
from django.contrib.postgres.fields import ArrayField

class Characters(models.Model):
    name_en = models.CharField(max_length=255)
    name_jp = models.CharField(max_length=255)
    age = models.IntegerField()
    birthdate = models.CharField(max_length=255)
    zodiac = models.CharField(max_length=255)
    affiliations = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    image = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name_en


class Units(models.Model):
    name_en = models.CharField(max_length=255)
    name_jp = models.CharField(max_length=255)
    model_type = models.CharField(max_length=255)
    pilot = models.CharField(max_length=255)
    soul = models.CharField(max_length=255)
    image = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name_en
    
class Evangelion(models.Model):
    title_en = models.CharField(max_length=255)
    title_jp = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    episodes = models.IntegerField()
    genre = ArrayField(
        ArrayField(
            models.CharField(max_length=255)
        )
    )
    released = models.CharField(max_length=255)
    logo = models.URLField(max_length=1024, null=True, blank=True)
    characters = models.ManyToManyField(Characters)
    evangelions = models.ManyToManyField(Units)
    
    def __str__(self):
        return self.title_en