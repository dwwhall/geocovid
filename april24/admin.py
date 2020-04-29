from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin

from .models import april24

@admin.register(april24)
class covidadmin1(OSMGeoAdmin):
	list_display = ('Province_State','Country_Region','confirmedApril24','location')





