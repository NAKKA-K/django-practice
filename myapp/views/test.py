# django import
from django.shortcuts import render

# app import
from myapp.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin

# views here

# 動作テスト中のコード================================
def regi_view(request):
  return render(request, 'myapp/forgotpassword.html')

def kadai_view(request):
  return render(request, 'myapp/kadaiform.html')

def login_view(request):
  return render(request, 'myapp/login.html')

class TestLogin(LoginRequiredMessageMixin):
  def get(request):
    return render(request, 'myapp/login.html')
