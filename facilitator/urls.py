from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('home/', views.home, name='home'),  # /home URL
]