from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *


class PartsHome(LoginRequiredMixin,ListView):
    model = Parts
    template_name = 'autoparts/index.html'
    context_object_name = 'parts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PartsCategory(LoginRequiredMixin,ListView):
    model = Parts
    template_name = 'autoparts/index.html'
    context_object_name = 'part'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ShowPart(LoginRequiredMixin,DetailView):
    model = Parts
    template_name = 'autoparts/part.html'
    slug_url_kwarg = 'part_slug'
    context_object_name = 'parts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
