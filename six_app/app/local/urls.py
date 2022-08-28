from django.urls import path
from .views import local

urlpatterns = [
    path('',local, name='local'),
]