from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.equipo.forms import EquipoForm
from apps.equipo.models import Equipo


class EquipoList(ListView):
    model = Equipo
    template_name = 'Equipo/equipo_list.html'
    paginate_by = 3

class EquipoCreate(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'Equipo/equipo_form.html'
    success_url = reverse_lazy('equipo:equipo_list')

class EquipoUpdate(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'Equipo/equipo_form.html'
    success_url = reverse_lazy('equipo:equipo_list')

class EquipoDelete(DeleteView):
    model = Equipo
    template_name = 'Equipo/equipo_delete.html'
    success_url = reverse_lazy('equipo:equipo_list')
