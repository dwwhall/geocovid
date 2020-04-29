from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import loc

latitude = 40.03602652514773
longitude = -100.1513671735611

user_location = Point(longitude, latitude,srid=4326)

class Home(generic.ListView):
	model = loc
	context_object_name = "loc"
	queryset = loc.objects.annotate(distance=Distance("Loc", user_location)).order_by("distance")
	template_name = "covid/index.html" 



