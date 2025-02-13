from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL
    path('events/', views.EventList.as_view(), name='event_list'),
    path('login/', views.login_view, name='login'),  # URL pattern for login_view
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('create_event/', views.create_event, name='create_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('facilitator_dashboard/', views.facilitator_dashboard, name='facilitator_dashboard'),
]