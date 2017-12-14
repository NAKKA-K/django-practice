from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^(?P<pk>[0-9]+)/$', views.detail, name = 'detail'),
  url(r'^new/$', views.PostNew.as_view(), name = 'new'),
  url(r'^(?P<pk>[0-9]+)/edit/$', views.PostUpdate.as_view(), name = 'edit'),
  url(r'^drafts/$', views.DraftList.as_view(), name = 'draft_list'),
  url(r'^(?P<pk>[0-9]+)/publish/$', views.PostPublish.as_view(), name = 'publish'),
  url(r'^(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name = 'delete'),

  url(r'^(?P<pk>[0-9]+)/comment/$', views.CommentCreate.as_view(), name = 'create_comment'),
  url(r'^(?P<pk>[0-9]+)/comment/approve/$', views.CommentApprove.as_view(), name = 'approve_comment'),
  url(r'^(?P<pk>[0-9]+)/comment/remove/$', views.CommentRemove.as_view(), name = 'remove_comment'),

  url(r'user_creation/$', views.AccountCreateView.as_view(), name='user_creation'),



  url(r'regi/$', views.regi_view, name = 'regi'),
  url(r'kadai/$', views.kadai_view, name = 'kadai'),
]
