from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'console', 'release_date']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'console': 'Consola',
            'release_date': 'Fecha de lanzamiento',
        }
