from django.shortcuts import render
import requests


def local(request):
    app_id = 'bc2ff5631b76496aada181625222408'
    city = "Ростов-на-Дону"
    url = f'http://api.weatherapi.com/v1/current.json?key={app_id}&q={city}&aqi=no'
    res = requests.get(url).json()
    context = {
        'name': res['location']['name'],
        'region': res['location']['region'],
        'localtime': res['location']['localtime'],
        'temp_c': res['current']['temp_c'],
        'icon': res['current']['condition']['icon'],
        'wind_speed': res['current']['wind_kph'],
        'wind_dir': res['current']['wind_dir']}
    print(res['location']['lat'])
    return render(request, template_name='local/local.html', context=context)

# http://api.weatherapi.com/v1/current.json?key=bc2ff5631b76496aada181625222408&q=London&aqi=no
# bc2ff5631b76496aada181625222408
