from django.contrib import admin

from .models import Bike, Service

# Register your models here.

admin.site.register(Bike)
admin.site.register(Service)