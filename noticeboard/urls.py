from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL
    path('events/', views.EventList.as_view(), name='event_list'),
    path('login/', views.login_view, name='login'),  # URL pattern for login_view
    path('logout/', views.logout_view, name='logout'),  # URL pattern for logout_view
    path('register/', views.create_community_user, name='create_community_user'),  # URL pattern for register
    path('event/<int:event_id>/', views.event_detail, name='event_detail'), # URL pattern for event_detail
    path('create_event/', views.create_event, name='create_event'), # URL pattern for create_event
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'), # URL pattern for edit_event
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),  # URL pattern for delete_event
    path('book_event/<int:event_id>/', views.book_event, name='book_event'),
    path('facilitator_dashboard/', views.facilitator_dashboard, name='facilitator_dashboard'), # URL pattern for facilitator_dashboard
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),  # URL pattern for user_dashboard
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),  # URL pattern for cancel_booking
]   
