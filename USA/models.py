from django.contrib.gis.db import models

# Create your models here.

class covid(models.Model):
	Province_State = models.CharField(max_length=100)
	Country_Region = models.CharField(max_length=100)
	Long = models.PointField()
	Lat = models.PointField()
	confirmedApril17 = models.CharField(max_length=100)
	deathsApril17 = models.CharField(max_length=100)
	recoveredApril17 = models.CharField(max_length=100)

class loc(models.Model):
	Province_State = models.CharField(max_length=100)
	Country_Region = models.CharField(max_length=100)
	confirmedApril17 = models.CharField(max_length=100)
	deathsApril17 = models.CharField(max_length=100)
	recoveredApril17 = models.CharField(max_length=100)
	Loc = models.PointField()
