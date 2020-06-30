from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login

from .models import Bike, Service
from .forms import Bike_Form, Service_Form, SignupForm

# Create your views here.

def home(request): 
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bikes_index(request):
  if request.method == 'POST':
    bike_form = Bike_Form(request.POST)
    if bike_form.is_valid:
      new_bike = bike_form.save(commit=False)
      new_bike.owner = request.user
      new_bike.save()
      return redirect('index')
  else:
    bike_form = Bike_Form()
  bikes = Bike.objects.filter(owner=request.user)
  context = {'bikes': bikes, 'bike_form': bike_form}
  return render(request, 'bikes/index.html', context)

def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  service_form = Service_Form()
  context = {'bike': bike, 'service_form': service_form}
  return render(request, 'bikes/show.html', context)

def bikes_edit(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  if request.method == 'POST':
    bike_form = Bike_Form(request.POST, instance = bike)
    if bike_form.is_valid():
      bike_form.save()
      return redirect('detail', bike_id=bike_id)
  else:
    bike_form = Bike_Form(instance=bike)
  context = {'bike': bike, 'bike_form': bike_form}
  return render(request, 'bikes/edit.html', context)

def bikes_delete(request, bike_id):
  Bike.objects.get(id=bike_id).delete()
  return redirect('index')

def add_service(request, bike_id):
  service_form = Service_Form(request.POST)
  if service_form.is_valid():
    new_service = service_form.save(commit=False)
    new_service.bike_id = bike_id
    new_service.save()
  return redirect('detail', bike_id=bike_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      login(request, user)
      return redirect('index')
    else: 
      error_message = 'Invalid signup please try again'
  else:
    form = SignupForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)