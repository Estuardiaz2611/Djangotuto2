from django import forms

from apps.equipo.models import Equipo

class EquipoForm (forms.ModelForm):

    class Meta:
        model = Equipo

        fields = [
            'nombre_equipo',
            'siglas',
            'jugadores',
            'encargado',
            'telefono',
            'liga',
        ]
        label = {
            'nombre_equipo': 'Nombre Liga',
            'siglas': 'Siglas',
            'jugadores': 'Jugadores',
            'encargado': 'Encargado',
            'telefono':  'Telefono',
            'liga': 'Liga',
        }
        widgets = {
            'nombre_equipo': forms.TextInput(attrs={'class':'form-control'}),
            'siglas': forms.TextInput(attrs={'class':'form-control'}),
            'jugadores': forms.TextInput(attrs={'class':'form-control'}),
            'encargado': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'liga': forms.Select(attrs={'class': 'form-control'})
        }