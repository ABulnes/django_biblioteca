from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm


class Index(TemplateView):
    template_name = 'index.html'


# CRUD de Autores


class ListAuthor(ListView):
    model = Author
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Author.objects.filter(state=True)


class UpdateAuthor(UpdateView):
    model = Author
    template_name = 'libro/autor/crear_autor.html'
    form_class = AuthorForm
    success_url = reverse_lazy('libro:listar_autor')


class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')


class DeleteAuthor(DeleteView):
    model = Author

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        object = Author.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('libro:listar_autor')


# CRUD de Libros

class ListBooks(View):
    model = Book
    form_class = BookForm
    template_name = 'libro/libro/listar_libro.html'

    def get_queryset(self):
        return self.model.objects.filter(state=True)

    def get_context_data(self, **kwargs):
        context = {
            'libros': self.get_queryset(),
            'form': self.form_class
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro:listado_libros')


class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')


class UpdateBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'libro/libro/libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = self.model.objects.filter(state=True)
        return context


class DeleteBook(DeleteView):
    model = Book

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        object = Book.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('libro:listado_libros')
