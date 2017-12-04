from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^(?P<pk>[0-9]+)/$', views.detail, name = 'detail'),
  url(r'^new/$', views.PostNew.as_view(), name = 'new'),
  url(r'^(?P<pk>[0-9]+)/edit/$', views.PostUpdate.as_view(), name = 'edit'),
]
