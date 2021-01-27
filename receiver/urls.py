from django.urls import path
from .views import *

urlpatterns = [
	path('getData/', Reader.as_view()),
	path('sendData/', writer),
	path('getPPM1/', writer),
	path('getPPM25/', writer),
	path('getPPM10/', writer),
	path('getTemperature/', TemperatureView.as_view()),
	path('getHumidity/', HumidityView.as_view()),
	path('getCO2/', CO2View.as_view()),
]