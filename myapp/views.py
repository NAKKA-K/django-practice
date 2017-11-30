from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import Post

# Create your views here.

def index(request):
  posts = get_list_or_404(Post)
  return render(request, 'myapp/index.html', {'posts': posts})
