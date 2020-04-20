from django.contrib import admin

# Register your models here.


from django.contrib.gis.admin import OSMGeoAdmin

from .models import covid
from .models import loc

@admin.register(covid)
class covidadmin1 (OSMGeoAdmin):
	list_display = ('Province_State','Country_Region', 'Lat','Long','confirmedApril17','deathsApril17','recoveredApril17')

@admin.register(loc)
class covidadmin1 (OSMGeoAdmin):
	list_display = ('Province_State','Country_Region','confirmedApril17','deathsApril17','recoveredApril17','Loc')
