from django.shortcuts import redirect, render
from .forms import GameForm


def home(request):
    contexto ={}
    return render (request,'index.html', contexto)

def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/home/')  
    else:
        form = GameForm()

    return render(request, 'agregar_game.html', {'form': form}) 