from django.contrib import admin
from .models.models import Evangelion, Characters, EvaUnits

admin.site.register(Evangelion)
admin.site.register(Characters)
admin.site.register(EvaUnits)