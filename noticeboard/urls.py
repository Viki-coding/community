from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('home/', views.home, name='home'),  # /home URL
    path('events/', views.EventList.as_view(), name='event_list'),
    path('login/', views.home, name='login'), 
    path('', views.index, name='index'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]