from django.urls import include, path
from blog.views import home, create_game

urlpatterns = [
path('home/', home, name= 'home'),
path('agregar/', create_game,name='agregar'),
]