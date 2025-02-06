from django import forms
from .models import Event

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'date',
            'starttime',
            'endtime',
            'location',
            'category',
            'excerpt',
            'description',
        ]
