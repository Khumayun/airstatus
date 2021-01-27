from rest_framework import serializers
from .models import *

class PMSerializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = '__all__'

class PM1Serializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = ['pm1']

class PM25Serializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = ['pm25']

class PM10Serializer(serializers.ModelSerializer):
	class Meta:
		model = PM
		fields = ['pm10']

class TemperatureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Temperature
		fields = '__all__'

class HumiditySerializer(serializers.ModelSerializer):
	class Meta:
		model = Humidity
		fields = '__all__'

class CO2Serializer(serializers.ModelSerializer):
	class Meta:
		model = CO2
		fields = '__all__'