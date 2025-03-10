from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, Location


# Create your tests here.
class EventModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        self.location = Location.objects.create(name='Main Hall')
        self.event = Event.objects.create(
            title='Test Event',
            date='2025-12-12',
            start_time='12:00',
            end_time='14:00',
            location=self.location,
            category='Other',
            excerpt='Test Event Excerpt',
            description='Test Event Description',
            capacity=100,
            booking_deadline='2025-12-11 12:00'
        )


def test_create_event_view(self):
    response = self.client.get('/events/create/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'noticeboard/event_form.html')
