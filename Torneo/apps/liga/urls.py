from django.conf.urls import url, include
from django.urls import path
from apps.liga.views import index, LigaList, LigaCreate, LigaUpdate, LigaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('principal/', index, name='liga_principal'),
    path('nuevo/', login_required( LigaCreate.as_view()), name='liga_create'),
    path('listar/', login_required(LigaList.as_view()), name='liga_list'),
    path('editar/(?P<pk>\d+)/', login_required(LigaUpdate.as_view()), name='liga_edit'),
    path('eliminar/(?P<pk>\d+)/', login_required(LigaDelete.as_view()), name='liga_delete'),
]
