from rest_framework import serializers
from .models import *

class PMSerializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = '__all__'

class PM1Serializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = ['id', 'pm1', 'time']

class PM25Serializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = ['id', 'pm25', 'time']

class PM10Serializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = ['id', 'pm10', 'time']

class PMsSerializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = ['id', 'pm1', 'pm25', 'pm10', 'time']

class TemperatureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Temperature
		fields = ['id', 'degree', 'time']

class HumiditySerializer(serializers.ModelSerializer):
	class Meta:
		model = Humidity
		fields = ['id', 'percent', 'time']

class CO2Serializer(serializers.ModelSerializer):
	class Meta:
		model = CO2
		fields = ['id', 'index', 'time']