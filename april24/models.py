from django.contrib.gis.db import models

# Create your models here.


class april24(models.Model):
	Province_State = models.CharField(max_length=100)
	Country_Region = models.CharField(max_length=100)
	confirmedApril24 = models.CharField(max_length=100)
	location = models.PointField()