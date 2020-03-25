from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre autor', max_length=200, blank=False, null=False)
    last_name = models.CharField('Apellido autor', max_length=220, blank=False, null=False)
    nationality = models.CharField('Nacionalidad', max_length=100, blank=False, null=False)
    description = models.TextField('Biografía', blank=True, null=True)
    state = models.BooleanField('Auto activo / No activo', default=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['id']

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=200, blank=False, null=False)
    publication_date = models.DateField('Fecha de publicación', blank=False, null=False)
    author = models.ManyToManyField(Author)
    creation_date = models.DateField(blank=False, null=False, auto_now=True, auto_now_add=False)
    state = models.BooleanField('Libro existente/No existente', default=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['title']

    def __str__(self):
        return self.title
