from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Post, Comment
from .forms import PostForm


# Create your views here.

class IndexView(ListView):
  model = Post
  template_name = 'myapp/index.html'

def index(request):
  posts = get_list_or_404(Post)
  return render(request, 'myapp/index.html', {'posts': posts})

def detail(request, pk):
  post = get_object_or_404(Post, pk = pk)
  return render(request, 'myapp/detail.html', {'post': post})

class PostNew(LoginRequiredMixin, FormView):
  form_class = PostForm
  template_name = 'myapp/new.html'
  
  def form_valid(self, form):
    post = form.save(commit = False) # 現在のフォーム内容をDBに登録せずに、戻り値で受け取る
    post.author = self.request.user
    post.save()
    # detailにpkにpost.pkを渡し、飛ばす
    return redirect('post:detail', pk = post.pk)

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ['title', 'text']
  template_name = 'myapp/edit.html'

class PostPublish(LoginRequiredMixin, UpdateView):
  def get(self, request, **kwargs):
    post = get_object_or_404(Post, pk = kwargs['pk'])
    post.publish()
    return redirect('post:detail', pk = post.pk)

class PostDelete(LoginRequiredMixin, DeleteView):
  def get(self, request, **kwargs):
    post = get_object_or_404(Post, pk = kwargs['pk'])
    post.delete()
    return redirect('post:index')


class DraftList(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'myapp/draft_list.html'

  def get_context_date(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['drafts'] = get_list_or_404(Post).filter(published_date__isnull=True).order_by('created_date')
    return context


class CommentCreate(CreateView):
  model = Comment
  fields = ['author', 'text']    
  template_name = 'myapp/create_comment.html'
