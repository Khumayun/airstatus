from django.db import models

class PM(models.Model):
	class Meta:
		verbose_name_plural = "PMs data"

	time = models.DateTimeField(auto_now = True)
	pm1 = models.IntegerField()
	pm25 = models.IntegerField()
	pm10 = models.IntegerField()

class Temperature(models.Model):
	class Meta:
		verbose_name_plural = "Temperature data"

	time = models.DateTimeField(auto_now = True)
	degree = models.IntegerField()

class Humidity(models.Model):
	class Meta:
		verbose_name_plural = "Humidity data"

	time = models.DateTimeField(auto_now = True)
	percent = models.IntegerField()

class CO2(models.Model):
	class Meta:
		verbose_name_plural = "CO2 data"

	time = models.DateTimeField(auto_now = True)
	index = models.IntegerField()