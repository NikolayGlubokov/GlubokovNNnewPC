from django.urls import path
from . import views

app_name = 'access'

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

]
