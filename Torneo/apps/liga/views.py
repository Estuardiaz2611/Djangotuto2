from django.shortcuts import render, redirect
from apps.liga.forms import LigaForm
from apps.liga.models import Liga
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'liga/index.html')

class LigaList(ListView):
    model = Liga
    template_name = 'liga/liga_list.html'
    paginate_by = 3

class LigaCreate(CreateView):
    model = Liga
    form_class = LigaForm
    template_name = 'liga/liga_form.html'
    success_url = reverse_lazy('liga:liga_list')

class LigaUpdate(UpdateView):
    model = Liga
    form_class = LigaForm
    template_name = 'liga/liga_form.html'
    success_url = reverse_lazy('liga:liga_list')

class LigaDelete(DeleteView):
    model = Liga
    template_name = 'liga/liga_delete.html'
    success_url = reverse_lazy('liga:liga_list')
