from django.contrib import admin
from .models import *

admin.site.register(PM)
admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(CO2)