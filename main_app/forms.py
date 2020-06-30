from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Bike, Service


class Bike_Form(ModelForm):

  class Meta: 
    model = Bike
    fields = ['name', 'make', 'model', 'purchaseDate', 'miles']

class Service_Form(ModelForm):

  class Meta: 
    model = Service
    fields = ['date', 'service']


class SignupForm(UserCreationForm):
  email = forms.EmailField(max_length=50)

  class Meta: 
    model = User
    fields = ('username', 'email', 'password1', 'password2')