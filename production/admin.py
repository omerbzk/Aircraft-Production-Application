from django.contrib import admin
from .models import Team, Personnel, AircraftType, Part, Aircraft

admin.site.register(Team)
admin.site.register(Personnel)
admin.site.register(AircraftType)
admin.site.register(Part)
admin.site.register(Aircraft)