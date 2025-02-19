from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .models import Event
from .forms import EventForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.text import slugify
from django.urls import reverse_lazy

# Check if the user is in the facilitator group
def is_facilitator(user):
    return user.groups.filter(name='Facilitators').exists()

# Create your views to display on notice.
# Creat a view to display if a filter is applied to the events
def index(request):
    category = request.GET.get('category')
    if category:
        events = Event.objects.filter(category=category)
    else:
        events = Event.objects.all()
    categories = Event.CATEGORY_CHOICES
    return render(request, 'noticeboard/index.html', {'events': events})  

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('-created') # order in descending order from the most recent to the oldest
    template_name = 'noticeboard/index.html'
    paginate_by = 3

# Create a view to handle login form using djangos built in authentication.
# If user is facilitator redirect to facilitator_dashboard
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_facilitator(user):
                return redirect('facilitator_dashboard')
            return redirect('index')
        else:
            return render(request, 'noticeboard/login.html', {'error': 'Invalid username or password'})
    return render(request, 'noticeboard/login.html')

# create a view to display the event details and description in full 
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_facilitator = request.user == event.facilitator
    return render(request, 'noticeboard/event_detail.html', {'event': event, 'is_facilitator': is_facilitator})

# Create a view to handle event creation, on dashboard page
@login_required
@user_passes_test(is_facilitator)
def create_event(request):
    """
    View to handle event creation by facilitators.
    Only logged-in users who are facilitators can access this view.
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.facilitator = request.user
            event.slug = slugify(event.title) 
            event.save()
            return redirect('facilitator_dashboard')
    else:
        form = EventForm()
    return render(request, 'noticeboard/create_event.html', {'form': form})

# Create a view to handle editing of events by facilitators
@login_required
@user_passes_test(is_facilitator)
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, facilitator=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event.slug = slugify(event.title) 
            form.save()
            return redirect('facilitator_dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'noticeboard/edit_event.html', {'form': form, 'event': event})

# Create a view to handle event deletion by facilitators
@login_required
@user_passes_test(is_facilitator)
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, facilitator=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('facilitator_dashboard')
    return render(request, 'noticeboard/delete_event.html', {'event': event})

# Create a view to for the facilitator dashboard
@login_required
@user_passes_test(is_facilitator)
def facilitator_dashboard(request):
    events = Event.objects.filter(facilitator=request.user)
    return render(request, 'noticeboard/facilitator_dashboard.html', {'events': events})

# Create a view to handle logout and confirm the facilitator wants to logout
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    return render(request, 'noticeboard/logout_confirm.html')

def handler404(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, 'errors/404.html', status=404)
