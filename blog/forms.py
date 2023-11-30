from django import forms
from .models import Comentario, Game, Opinion

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
    
class BuscarGame(forms.Form):
    game_title = forms.CharField(label='Nombre del juego',max_length=100, required=True)

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['game', 'rating', 'opinion']
        labels = {
            'game': 'Juego',
            'rating': 'Calificación',
            'opinion': 'Opinión'
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['game','autor_name','comentario','date']
        labels = {
            'game': 'Juego',
            'autor_name': 'Tu nombre',
            'comentario': 'Agrega un comentario',
            'date': 'Fecha'
        }