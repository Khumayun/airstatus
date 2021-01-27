from django.urls import path
from .views import *

urlpatterns = [
	path('getData/', Reader.as_view()),
	path('sendData/', writer),
	path('getPPM1/', PM1View.as_view()),
	path('getPPM25/', PM25View.as_view()),
	path('getPPM10/', PM10View.as_view()),
	path('getTemperature/', TemperatureView.as_view()),
	path('getHumidity/', HumidityView.as_view()),
	path('getCO2/', CO2View.as_view()),
]