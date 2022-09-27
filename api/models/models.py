from django.db import models
from django.contrib.postgres.fields import ArrayField

class Characters(models.Model):
    name_en = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    name_jp = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    age = models.IntegerField()
    birthdate = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    zodiac = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    affiliations = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    title = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    height = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    weight = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    image = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name_en
    
class EvaUnits(models.Model):
    name_en = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    name_jp = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    model_type = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    pilot = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    soul = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    image = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name_en


class Evangelion(models.Model):
    title_en = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    title_jp = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    type = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    episodes = models.IntegerField()
    genre = ArrayField(models.CharField(max_length=255, null=True))
    released = models.CharField(max_length=50, blank=False, null=False, default='N/A')
    logo = models.URLField(max_length=1024, null=True, blank=True)
    characters = models.ManyToManyField(Characters, blank=True, related_name="Chars")
    units = models.ManyToManyField(EvaUnits, blank=True, related_name="Evas")

    def __str__(self):
        return self.title_en