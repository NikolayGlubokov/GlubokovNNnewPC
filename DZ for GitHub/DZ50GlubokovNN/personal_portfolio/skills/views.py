from django.shortcuts import render
from .models import Skills
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects':projects})
# Create your views here.
