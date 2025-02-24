from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import CommunityUser, Event


# CommunityUser SignUp Form
class CommunityUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15, required=True, help_text="Enter your phone number.")

    class Meta:
        model = User
        fields = ['username', 'email', 'telephone', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super.save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            CommunityUser.objects.create(user=user, telephone=self.cleaned_data['telephone'])
        return user

class EventForm(forms.ModelForm):
    date = forms.DateField(
        label='Date (dd/mm/yy)',
        widget=forms.DateInput(format='%d/%m/%y', attrs={'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%y']
    )

    start_time = forms.TimeField(
        label='Start Time (24hr format)',
        widget=forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'})
    )

    end_time = forms.TimeField(
        label='End Time (24hr format)',
        widget=forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'})
    )

    booking_deadline = forms.DateTimeField(
        label='Booking Deadline (dd/mm/yyyy hh:mm)',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%d/%m/%y %H:%M']
    )
    
    class Meta:
        model = Event
        fields = ['title', 'date', 'start_time', 'end_time', 'location', 'category', 'excerpt', 'description', 'capacity', 'booking_deadline']  
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Event Title'}),
            'start_time': forms.TimeInput(attrs={'placeholder': 'Start Time (24hr format)'}),
            'end_time': forms.TimeInput(attrs={'placeholder': 'End Time (24hr format)'}),
            'location': forms.Select(attrs={'placeholder': 'Select Location'}),
            'category': forms.Select(attrs={'placeholder': 'Select Category'}),
            'excerpt': forms.Textarea(attrs={'placeholder': 'Short Event Summary'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Maximum Participants'}),
            'booking_deadline': forms.DateTimeInput(attrs={'placeholder': 'Booking Deadline (dd/mm/yyyy hh:mm)'})   
        }