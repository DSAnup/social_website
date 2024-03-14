from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('edit/', views.edit, name='edit'),
    path('login_cancel/', views.login_cancel, name='login_cancel'),
    path('register/', views.register, name='register'),
]