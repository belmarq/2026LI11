from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from mi_aplicacion.models import Escuela, Maestro
from mi_aplicacion.forms import EscuelaForm, MaestroForm, UsuarioForm
from django.contrib.auth.models import User

class Home(View):
    def get(self, request):
        cdx={
        "titulo":"Home",
        "subtitulo":"Bienvenido a mi primer aplicación"
        }
        return render(request, "home/home.html", cdx)

class Usuarios(View):
    def get(self, request):
        usuarios = User.objects.all()
        cdx={
            "titulo":"Usuarios",
            "subtitulo":"Listado de usuarios",
            "usuarios": usuarios}
        return render(request, "usuarios/usuarios.html", cdx)
 
class UsuarioAlta(View):
    def get(self, request):
        cdx={
        "titulo":"Usuarios",
        "subtitulo":"Alta de usuario",
        "texto_boton":"Guardar",
        "fondo":"bg-success bg-opacity-25 p-3",
        "form":UsuarioForm()
        }
        return render(request, 'usuarios/CRUD.html', cdx)
    
    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            cdx={
                "titulo":"Altas de usuario",
                "subtitulo":"Alta de usuario",
                "texto_boton":"Guardar",
                "form":form,
                "fondo":"bg-success bg-opacity-25 p-3",
                "mensaje":"Error al crear el usuario"
            }
        return render(request, 'usuarios/CRUD.html', cdx)

class UsuarioEditar(View):
    def get(self, request, id):
        usuario = User.objects.filter(id=id).first()
        form = UsuarioForm(instance=usuario)
        cdx={
        "titulo":"Usuarios",
        "subtitulo":"Editar usuario",
        "texto_boton":"Actualizar",
        "fondo":"bg-warning bg-opacity-25 p-3",
        "form":form
        }
        return render(request, 'usuarios/CRUD.html', cdx)
    
    def post(self, request, id):
        usuario = User.objects.filter(id=id).first()
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        return redirect("home")         


class UsuarioEliminar(View):
    def get(self, request, id):
        usuario = User.objects.filter(id=id).first()
        form = UsuarioForm(instance=usuario)
        cdx={
        "titulo":"Usuarios",
        "subtitulo":"Eliminar usuario",
        "texto_boton":"Eliminar",
        "form":form,
        "fondo":"bg-danger bg-opacity-25 p-3"
        }
        return render(request, 'usuarios/CRUD.html', cdx)
    
    def post(self, request, id):
        usuario = User.objects.filter(id=id).first()
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario.delete()
            return redirect('usuarios')
        return redirect("home")


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
        "maestros":maestros,
        "escuelas":Escuela.objects.all()
        }
        return render(request, "maestros/maestros.html", cdx)
    
    def post(self, request):
        if not request.user.has_perm('mi_aplicacion.view_maestro'):
            messages.error(request, "No tienes permiso para ver la página de maestros.")
            return redirect("home")
        # print(f"Datos recibidos: {request.POST}")
        nombre = request.POST.get("nombre", "")
        escuela_id = request.POST.get("escuela", "0")
        escuela_id = int(escuela_id)
        maestros = Maestro.objects.all()
        # print(f"Maestros antes de filtrar: {maestros}")
        if nombre:
            maestros = maestros.filter(nombre__icontains=nombre)
        # print(f"Maestros después de filtrar por nombre: {maestros}")
        if escuela_id != 0:
            maestros = maestros.filter(escuela_id=escuela_id)
        # print(f"Maestros después de filtrar por escuela: {maestros}")
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Lista de maestros",
        "maestros":maestros,
        "escuelas":Escuela.objects.all()
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