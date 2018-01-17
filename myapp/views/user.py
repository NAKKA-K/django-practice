# django import
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic.edit import CreateView

# app import


# views here

# User管理 ==============================================

class AccountCreateView(CreateView):
  """
  This view is default.
  If want to change the Model, inherit the User Model.
  template_name is default. It is the myapp/auth/user_form.html.
  """
  model = User
  form_class = UserCreationForm

  def get_success_url(self):
    return reverse('login')

