"""定义learning_logs的URL模式"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
	path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout', views.logout_view, name='logout'),
	path('register', views.register, name='register'),
]