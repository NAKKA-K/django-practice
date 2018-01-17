# django import
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# app import
from myapp.models import Comment
from myapp.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin


# views here

# Comment処理 ============================================

class CommentCreate(CreateView):
  model = Comment
  fields = ['author', 'text']    
  template_name = 'myapp/create_comment.html'

  def form_valid(self, form):
    comment = form.save(commit = False)
    comment.post = get_object_or_404(Post, pk = self.kwargs['pk'])
    comment.save()
    return redirect('post:detail', pk = comment.post.pk)

class CommentApprove(LoginRequiredMessageMixin, UpdateView):
  def get(self, request, **kwargs):
    comment = get_object_or_404(Comment, pk = kwargs['pk'])
    comment.approve()
    return redirect('post:detail', pk = comment.post.pk)

class CommentRemove(LoginRequiredMessageMixin, DeleteView):
  def get(self, request, **kwargs):
    comment = get_object_or_404(Comment, pk = kwargs['pk'])
    comment.delete()
    return redirect('post:detail', pk = comment.post.pk)

