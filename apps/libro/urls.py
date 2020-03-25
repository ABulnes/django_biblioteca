from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('listar_autor/', login_required(ListAuthor.as_view()), name='listar_autor'),
    path('editar_autor/<int:pk>', login_required(UpdateAuthor.as_view()), name='editar_autor'),
    path('crear_autor/', login_required(CreateAuthor.as_view()), name='crear_autor'),
    path('eliminar_autor/<int:pk>', login_required(DeleteAuthor.as_view()), name='eliminar_autor'),
    path('listar_libros/', login_required(ListBooks.as_view()), name='listado_libros'),
    path('editar_libro/<int:pk>', login_required(UpdateBook.as_view()), name='editar_libro'),
    path('eliminar_libro/<int:pk>', login_required(DeleteBook.as_view()), name='eliminar_libro'),
    path('crear_libro/', login_required(CreateBook.as_view()), name='crear_libro'),
]
