from django.shortcuts import render

def home(request):
    return render(request, 'facilitator/home.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

