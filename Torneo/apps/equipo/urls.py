from django.conf.urls import url, include
from django.urls import path
from apps.equipo.views import Equipo, EquipoList, EquipoCreate, EquipoUpdate, EquipoDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('nuevo/', login_required(EquipoCreate.as_view()), name='equipo_create'),
    path('listar/', login_required(EquipoList.as_view()), name='equipo_list'),
    path('editar/<int:pk>)/', login_required(EquipoUpdate.as_view()), name='equipo_edit'),
    path('eliminar/<int:pk>)/', login_required(EquipoDelete.as_view()), name='equipo_delete'),
]
