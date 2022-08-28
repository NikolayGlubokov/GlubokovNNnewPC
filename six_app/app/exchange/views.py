from django.shortcuts import render
import requests


def exchange(request):
    response = requests.get(url='https://cdn.cur.su/api/latest.json').json()
    currencies = response.get('rates')
    if request.method == 'GET':
        context = {
            'currencies': currencies
        }

        return render(request, template_name='exchange/index.html', context=context)
    if request.method == 'POST':
        form_amount = float(request.POST.get('form-amount'))

        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * form_amount, 2)
        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'form_amount': str(form_amount),
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request, template_name='exchange/index.html', context=context)
