from django.urls import include, path
from blog.views import buscar_game, crear_comentario, crear_opinion, home, create_game, individual_game

urlpatterns = [
path('home/', home, name= 'home'),
path('agregar/', create_game,name='agregar'),
path('buscar/', buscar_game, name = 'buscar'),
path('agregar_opinion/', crear_opinion, name ='agregar_opinion'),
path('individual_game/<int:game_id>/', individual_game, name = 'individual_game'),
path('agregar_comentario/', crear_comentario, name ='agregar_comentario')
]