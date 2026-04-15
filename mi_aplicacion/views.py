from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from mi_aplicacion.models import Escuela, Maestro
from mi_aplicacion.forms import EscuelaForm, MaestroForm

class Home(View):
    def get(self, request):
        cdx={
        "titulo":"Home",
        "subtitulo":"Bienvenido a mi primer aplicación"
        }
        return render(request, "home/home.html", cdx)

class Escuelas(View):
    def get(self, request):
        escuelas = Escuela.objects.all()
        cdx={
        "titulo":"Escuelas",
        "subtitulo":"Lista de escuelas",
        "escuelas":escuelas
        }
        return render(request, "escuelas/escuelas.html", cdx)

class EscuelaAlta(View):
    def get(self, request):
        form = EscuelaForm()
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Alta de Escuela",
        "form":form
        }
        return render(request, 'escuelas/CRUD.html', cdx)
    
    def post(self, request):
        form = EscuelaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")
    
class EscuelaEditar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Edición de Escuela",
        "form":form
        }
        return render(request, 'escuelas/CRUD.html', cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")

    
class EscuelaEliminar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
        "titulo":"Escuela",
        "subtitulo":"Eliminación de Escuela",
        "form":form
        }
        return render(request, 'escuelas/CRUD.html', cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            escuela.delete()
            return redirect('escuelas')
        return redirect("home")

class Maestros(View):
    def get(self, request):
        if not request.user.has_perm('mi_aplicacion.view_maestro'):
            messages.error(request, "No tienes permiso para ver la página de maestros.")
            return redirect("home")
        maestros = Maestro.objects.all()
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Lista de maestros",
        "maestros":maestros
        }
        return render(request, "maestros/maestros.html", cdx)

class MaestroAlta(View):
    def get(self, request):
        if not request.user.has_perm('mi_aplicacion.add_maestro'):
            messages.error(request, "No tienes permiso para agregar maestros.")
            return redirect("home")
        form = MaestroForm()
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Alta de Maestro",
        "form":form,
        "fondo_formulario":"bg-success p-3",
        "texto_submit":"Guardar",
        }
        return render(request, 'maestros/CRUD.html', cdx)
    
    def post(self, request):
        form = MaestroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Alta de Maestro",
        "form":form,
        "fondo_formulario":"bg-success p-3",
        "texto_submit":"Guardar",
        }
        return render(request, 'maestros/CRUD.html', cdx)
    
class MaestroEditar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro)
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Edición de Maestro",
        "form":form,
        "fondo_formulario":"bg-warning p-3",
        "texto_submit":"Actualizar",
        }
        return render(request, 'maestros/CRUD.html', cdx)
    
    def post(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Edición de Maestro",
        "form":form,
        "fondo_formulario":"bg-warning p-3",
        "texto_submit":"Actualizar",
        }
        return render(request, 'maestros/CRUD.html', cdx)
    
class MaestroEliminar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro)
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Eliminación de Maestro",
        "form":form,
        "fondo_formulario":"bg-danger p-3",
        "texto_submit":"Eliminar",
        }
        return render(request, 'maestros/CRUD.html', cdx)
    
    def post(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            maestro.delete()
            return redirect('maestros')
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Eliminación de Maestro",
        "form":form,
        "fondo_formulario":"bg-danger p-3",
        "texto_submit":"Eliminar",
        }
        return render(request, 'maestros/CRUD.html', cdx)