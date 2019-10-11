from django import forms

from apps.liga.models import Liga

class LigaForm  (forms.ModelForm):

    class Meta:
        model = Liga

        fields = [
            'nombre_liga',
            'genero',
            'categoria',
            'jugadores',
            'fecha_inicio',
        ]
        label = {
            'nombre_liga': 'Nombre Liga',
            'genero': 'Genero',
            'categoria': 'Categoria',
            'jugadores': 'Jugadores',
            'fecha_inicio': 'Fecha Inicio',
        }
        widgets = {
            'nombre_liga': forms.TextInput(attrs={'class':'form-control'}),
            'genero': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'jugadores': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class':'form-control'}),
        }