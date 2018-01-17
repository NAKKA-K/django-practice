# django import
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

# app import
from myapp.models import Post


# views here

class IndexView(ListView):
  model = Post
  template_name = 'myapp/index.html'
  context_object_name = 'posts'


def detail(request, pk):
  post = get_object_or_404(Post, pk = pk)
  return render(request, 'myapp/detail.html', {'post': post})
