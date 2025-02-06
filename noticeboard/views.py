from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'noticeboard/index.html'
    paginate_by = 3
    
def home(request):
    return render(request, 'noticeboard/home.html')




