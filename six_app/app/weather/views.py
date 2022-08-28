from django.shortcuts import render
import requests


def weather(request):
    app_id = 'bc2ff5631b76496aada181625222408'
    city = "Москва"
    url = f'http://api.weatherapi.com/v1/current.json?key={app_id}&q={city}&aqi=no'
    res = requests.get(url).json()
    print(res)
    print(res['location']['lat'])
    return render(request, template_name='weather/weather.html')

# http://api.weatherapi.com/v1/current.json?key=bc2ff5631b76496aada181625222408&q=London&aqi=no
# bc2ff5631b76496aada181625222408
