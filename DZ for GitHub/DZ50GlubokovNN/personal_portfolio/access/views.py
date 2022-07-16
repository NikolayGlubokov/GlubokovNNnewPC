from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('access:loginuser')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'access/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'access/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('index')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'access/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')


            except IntegrityError:
                return render(request, 'access/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'Такое имя пользователя уже существует. Задайте другое.'})

        else:
            return render(request, 'access/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})
