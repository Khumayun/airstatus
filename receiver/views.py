from .models import *
from .serializers import *
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework import status
import datetime

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

@api_view(['POST', 'GET'])
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

class PM1View(ListAPIView):
	serializer_class = PM1Serializer
	def get_queryset(self):
		dateA = self.request.GET.get('time_start')
		dateB = self.request.GET.get('time_end')
		queryset = PM.objects.filter(time__range=(dateA, dateB))
		return queryset

class PM25View(ListAPIView):
	serializer_class = PM25Serializer
	def get_queryset(self):
		dateA = self.request.GET.get('time_start')
		dateB = self.request.GET.get('time_end')
		queryset = PM.objects.filter(time__range=(dateA, dateB))
		return queryset

class PM10View(ListAPIView):
	serializer_class = PM10Serializer
	def get_queryset(self):
		dateA = self.request.GET.get('time_start')
		dateB = self.request.GET.get('time_end')
		queryset = PM.objects.filter(time__range=(dateA, dateB))
		return queryset

class TemperatureView(ListAPIView):
	serializer_class = TemperatureSerializer
	def get_queryset(self):
		dateA = self.request.GET.get('time_start')
		dateB = self.request.GET.get('time_end')
		queryset = Temperature.objects.filter(time__range=(dateA, dateB))
		return queryset

class HumidityView(ListAPIView):
	serializer_class = HumiditySerializer
	def get_queryset(self):
		dateA = self.request.GET.get('time_start')
		dateB = self.request.GET.get('time_end')
		queryset = Humidity.objects.filter(time__range=(dateA, dateB))
		return queryset

class CO2View(ListAPIView):
	serializer_class = CO2Serializer
	def get_queryset(self):
		dateA = self.request.GET.get('time_start')
		dateB = self.request.GET.get('time_end')
		queryset = CO2.objects.filter(time__range=(dateA, dateB))
		return queryset