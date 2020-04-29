from django.shortcuts import render

# Create your views here.


from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import april24

longitude=-100.1513671735611

latitude=40.03602652514773

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
	model = april24
	context_object_name = "april24"
	queryset = april24.objects.annotate(distance=Distance("location", user_location)).order_by("distance")
	template_name = "covid/index.html" 

