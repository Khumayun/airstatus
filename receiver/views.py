from .models import *
from .serializers import *
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class Reader(ObjectMultipleModelAPIView):
	querylist = [
	{
		'queryset': PM.objects.all(),
		'serializer_class': PMSerializer
	},
	{
		'queryset': Temperature.objects.all(),
		'serializer_class': TemperatureSerializer
	},
	{
		'queryset': Humidity.objects.all(),
		'serializer_class': HumiditySerializer
	},
	{
		'queryset': CO2.objects.all(),
		'serializer_class': CO2Serializer
	}]

@api_view(['POST'])
def writer(request):
	serializer = PMSerializer(PM.objects.all(), many = True)
	if request.method == 'POST':
		pm1 = request.data['pm1']
		pm25 = request.data['pm25']
		pm10 = request.data['pm10']
		pm_data = PMSerializer(data = {'pm1': pm1, 'pm25': pm25, 'pm10': pm10})
		if pm_data.is_valid():
			pm_data.save()

		temperature = request.data['temperature']
		temperature_data = TemperatureSerializer(data = {'degree': temperature})
		if temperature_data.is_valid():
			temperature_data.save()

		humidity = request.data['humidity']
		humidity_data = HumiditySerializer(data = {'percent': humidity})
		if humidity_data.is_valid():
			humidity_data.save()

		co2 = request.data['co2']
		co2_data = CO2Serializer(data = {'index': co2})
		if co2_data.is_valid():
			co2_data.save()

		return Response(status=status.HTTP_201_CREATED)