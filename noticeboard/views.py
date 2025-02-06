
from django.views import generic
from .models import Event
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm

# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'noticeboard/index.html'
    paginate_by = 3

def home(request):
    return render(request, 'noticeboard/home.html')




