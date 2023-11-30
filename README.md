# PRE_ENTREGA
Este proyecto crea una página de reseñas de videojuegos, donde un usuario puede registrar un juego, y alguien más puede calificarlo o hacer comentarios al respecto.

## Requisitos Previos

- Python 3.11
- Django

# Instalación
- Clona el repositorio en local: 'git clone https://github.com/manuuelongo/PRE_ENTREGA.git'.
- Crear y activar el entorno virtual.
- Ejecuta las migraciones: 'python manage.py migrate'
- Inicia el servidor: 'python manage.py runserver'

#Uso
En la url blog/home se pueden ver todos los juegos que se han agregado para reseña, además se puede ingresar al juego para ver las opiniones y comentarios que ha tenido. 
Luego, en la barra superior están todas las opciones disponibles:
  - Gamerpedia: te lleva al inicio de la página.
  - Agregar Juego: se puede agregar un juego a la página (agregar nombre del juego, consola, descripción y fecha de lanzamiento)
  - Buscar Juego: busca un juego por nombre.
  - Opinion: Permite agregar una calificación y opinión sobre un juego.
  - Comentario: permite comentar respecto al juego.

#Estructura del proyecto
Los directorios principales del proyecto son "Pre_entrega" donde se encuentra la base del proyecto y "blog" que es la aplicación donde se desarrolló el resto de contenido de la página. 
En la carpeta templates se encuentra una sub-carpeta llamada base donde está el html correspondiente a la barra de navegación y pie de página.


