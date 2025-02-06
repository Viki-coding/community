
from django.views import generic
from .models import Event
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'noticeboard/event_list.html', {'events': events})   

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('-created')
    template_name = 'noticeboard/event.html'
    paginate_by = 3

def home(request):
    return render(request, 'noticeboard/event.html')


