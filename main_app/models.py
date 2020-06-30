from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Bike(models.Model):
  name = models.CharField(max_length=50)
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  purchaseDate = models.DateField()
  miles = models.IntegerField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} the {self.make} {self.model}'

SERVICES = (
  ('T', 'Tune Up'), 
  ('P', 'Tire Pressure Check'),
  ('C', 'Chain Clean and Grease'), 
  ('R', 'Repair') 
)

class Service(models.Model):
  date = models.DateField('Service Date')
  service = models.CharField(max_length=1, choices=SERVICES, default=SERVICES[0][0])
  bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='services')

  def __str__(self):
    return f'{self.get_service_display()} performed on {self.bike} on {self.date}'

  class Meta: 
    ordering = ['-date', 'service']