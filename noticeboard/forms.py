from django import forms
from django.contrib.auth.models import UserCreationForm
from .models import CommunityUser, Event

# CommunityUser SignUp Form
class CommunityUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(CommunityUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            CommunityUser.objects.create(user=user)
        return user

class EventForm(forms.ModelForm):
    date = forms.DateField(
        label='Date (dd/mm/yy)',
        widget=forms.DateInput(format='%d/%m/%y', attrs={'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%y']
    )
    
    class Meta:
        model = Event
        fields = ['title', 'date', 'start_time', 'end_time', 'location', 'category', 'excerpt', 'description', 'capacity', 'booking_deadline']  
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Event Title'}),
            'start_time': forms.TimeInput(attrs={'placeholder': 'Start Time (24hr format)'}),
            'end_time': forms.TimeInput(attrs={'placeholder': 'End Time (24hr format)'}),
            'location': forms.Select(attrs={'placeholder': 'Location'}),
            'category': forms.Select(attrs={'placeholder': 'Category'}),
            'excerpt': forms.Textarea(attrs={'placeholder': 'Short Description'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Maximum Capacity'}),
            'booking_deadline': forms.DateTimeInput(attrs={'placeholder': 'Booking Deadline (dd/mm/yyyy hh:mm)'})   
        }