from django.urls import path
from .views import *

urlpatterns = [
	path('getData/', Reader.as_view()),
	path('sendData/', writer),
]