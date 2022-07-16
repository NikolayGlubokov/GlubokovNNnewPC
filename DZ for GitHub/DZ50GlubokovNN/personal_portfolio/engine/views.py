from django.shortcuts import render, get_object_or_404
from .models import Engine
from django.contrib.auth.decorators import login_required

@login_required
def engine(request):
    engines = Engine.objects.all()
    return render(request, 'engine/engines.html', {'engines': engines})

@login_required
def details(request, engine_id):
    engine = get_object_or_404(Engine, pk=engine_id)
    return render(request, 'engine/details.html', {'engine': engine})
