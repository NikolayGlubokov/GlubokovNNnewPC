from django.shortcuts import render
from django.http import HttpResponse
import random



menu = [{'name': 'Об авторе', 'url': 'info'},
        {'name': 'Сгенерировать пароль', 'url': ''}]

lst2 = list(range(6, 15))
def home(request):
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):
    char = [chr(i) for i in range(97, 123)]

    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])
    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])
    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])
    psw = ''
    length = int(request.GET.get('length'))
    for i in range(length):
        psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})


def info(request):
    return render(request, 'generator/info.html', {'lst': lst2})
# Create your views here.
