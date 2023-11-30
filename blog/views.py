from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Comentario, Opinion, Game
from .forms import ComentarioForm, GameForm, BuscarGame, OpinionForm


def home(request):
    games = Game.objects.all()
    return render(request,'index.html',{'games':games})

def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = GameForm()

    return render(request, 'agregar_game.html', {'form': form}) 

def buscar_game(request):
    nombre = request.GET.get("game_title")
    if nombre is not None:
        games = Game.objects.filter(title__icontains=nombre)
    else:
        games = []
    contexto = {
        "games": games,
        "form":BuscarGame(initial={"game_title": nombre})
    }
    return render(request, "busqueda.html", contexto)

def crear_opinion(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save()
            game_id = opinion.game.id
            return redirect('individual_game', game_id=game_id)
    else:
        form = OpinionForm()
    return render(request, 'opiniones.html', {'form': form})

def individual_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    opiniones = Opinion.objects.filter(game=game)
    comentarios = Comentario.objects.filter(game=game)
    contexto = {
        "game": game,
        "opiniones": opiniones,
        "comentarios": comentarios
    }
    return render(request, "individual_game.html", contexto)

def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save()
            game_id = comentario.game.id
            return redirect ('individual_game', game_id = game_id)
    else:
        form = ComentarioForm()
    return render(request,'comentarios.html',{'form':form})
