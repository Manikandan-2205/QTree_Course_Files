from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.login, name='login'),
]