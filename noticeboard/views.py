
from django.views import generic
from .models import Event
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'noticeboard/index.html', {'events': events})  

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('-created') #order in descending order from the most recent to the oldest
    template_name = 'noticeboard/index.html'
    paginate_by = 3

# filepath: /Users/vikimulhall/Documents/community/noticeboard/views.py
from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

