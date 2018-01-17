# django import
from django.shortcuts import redirect, get_list_or_404, get_object_or_404 
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView

# app import
from myapp.forms import PostForm
from myapp.models import Post
from myapp.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin

# views here

# Post処理=======================================================
class PostNew(LoginRequiredMessageMixin, FormView):
  form_class = PostForm
  template_name = 'myapp/new.html'
  
  def form_valid(self, form):
    post = form.save(commit = False) # 現在のフォーム内容をDBに登録せずに、戻り値で受け取る
    post.author = self.request.user
    post.save()
    # detailにpkにpost.pkを渡し、飛ばす
    return redirect('post:detail', pk = post.pk)


class PostUpdate(LoginRequiredMessageMixin, UpdateView):
  model = Post
  fields = ['title', 'text']
  template_name = 'myapp/edit.html'


class PostPublish(LoginRequiredMessageMixin, UpdateView):
  def get(self, request, **kwargs):
    post = get_object_or_404(Post, pk = kwargs['pk'])
    post.publish()
    return redirect('post:detail', pk = post.pk)


class PostDelete(LoginRequiredMessageMixin, DeleteView):
  def get(self, request, **kwargs):
    post = get_object_or_404(Post, pk = kwargs['pk'])
    post.delete()
    return redirect('post:index')


class DraftList(LoginRequiredMessageMixin, ListView):
  model = Post
  template_name = 'myapp/draft_list.html'

  def get_context_date(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['drafts'] = get_list_or_404(Post).filter(published_date__isnull=True).order_by('created_date')
    return context

