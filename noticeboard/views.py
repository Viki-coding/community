
from django.views import generic
from django.contrib.auth import authenticate, login
from .models import Event
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'noticeboard/index.html', {'events': events})  

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('-created') # order in descending order from the most recent to the oldest
    template_name = 'noticeboard/index.html'
    paginate_by = 3

def home(request):
    events = Event.objects.all()
    return render(request, 'noticeboard/index.html', {'events': events})

# Create a view to handle login form using djangos built in authentication.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'noticeboard/index.html', {'error': 'Invalid credentials'})
    events = Event.objects.all()
    return render(request, 'noticeboard/index.html', {'events': events})

# create a view to display the event details and description in full 
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'noticeboard/event_detail.html', {'event': event})