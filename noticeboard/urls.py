from django.contrib import admin    # Import admin module
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('home/', views.home, name='home'),  # /home URL
    path('events/', views.EventList.as_view(), name='event_list'),
]