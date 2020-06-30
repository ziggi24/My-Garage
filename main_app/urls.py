from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.forms import AuthenticationForm

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bikes/', views.bikes_index, name='index'),
  path('bikes/<int:bike_id>/', views.bikes_detail, name='detail'),
  path('bikes/<int:bike_id>/delete', views.bikes_delete, name='delete'), 
  path('bikes/<int:bike_id>/edit', views.bikes_edit, name='edit'), 
  path('bikes/<int:bike_id>/add_service', views.add_service, name='add_service'),
]