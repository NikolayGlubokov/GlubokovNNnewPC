from django.urls import path
from . import views

app_name = 'engine'

urlpatterns = [
    path('', views.engine, name='engines'),
    path('<int:engine_id>/', views.details, name='detail'),

]