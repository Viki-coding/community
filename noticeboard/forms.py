from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(
        label='Date (dd/mm/yy)',
        widget=forms.DateInput(format='%d/%m/%y', attrs={'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%y']
    )
    
    class Meta:
        model = Event
        fields = ['title', 'date', 'start_time', 'end_time', 'location', 'category', 'excerpt', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Event Title'}),
            'starttime': forms.TimeInput(attrs={'placeholder': 'Start Time (24hr format)'}),
            'endtime': forms.TimeInput(attrs={'placeholder': 'End Time (24hr format)'}),
            'location': forms.Select(attrs={'placeholder': 'Location'}),
            'category': forms.Select(attrs={'placeholder': 'Category'}),
            'excerpt': forms.Textarea(attrs={'placeholder': 'Short Description'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
        }